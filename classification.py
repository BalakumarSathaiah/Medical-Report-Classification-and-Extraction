from transformers import pipeline
import nltk


def split_into_sentences(text):
    return nltk.tokenize.sent_tokenize(text)


# Initialize zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Step 5: Classify each chunk and sentence with validation
def classify_text(text, candidate_labels):
    sentence_classifications = {}
    confidence_threshold = 0.50  # Threshold for filtering out low-confidence results

    for sentence in split_into_sentences(text):
        result = classifier(sentence, candidate_labels)
        high_confidence_results = [
            {"label": label, "score": score, "content": sentence}
            for label, score in zip(result["labels"], result["scores"])
            if score >= confidence_threshold
        ]

        for classification in high_confidence_results:
            if (sentence not in sentence_classifications) or (
                classification["score"] > sentence_classifications[sentence]["score"]
            ):
                sentence_classifications[sentence] = classification

    return list(sentence_classifications.values())

# Function to merge similar sections based on label
def merge_similar_sections(formatted_output):
    merged = []
    seen_labels = {}

    for entry in formatted_output:
        label = entry["label"]
        content = entry["content"]
        score = entry["score"]

        # Ensure unique sections by merging them based on label
        if label in seen_labels:
            seen_labels[label]["content"] += "\n" + content  # Separate merged content with a newline
            seen_labels[label]["score"] = max(score, seen_labels[label]["score"])
        else:
            seen_labels[label] = {"content": content, "score": score}

    # Output merged sections
    for label, data in seen_labels.items():
        merged.append(
            f"{label} - {label} (Confidence: {data['score']:.2f})\nContent: {data['content']}\n"
        )

    return merged
