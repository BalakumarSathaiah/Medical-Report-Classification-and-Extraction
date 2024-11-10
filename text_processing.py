import re
import nltk

# Download punkt data without output (to suppress download messages)
nltk.download('punkt', quiet=True)

# Step 3: Clean and normalize text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()  # Replace multiple spaces with a single space
    return text.lower()  # Convert text to lowercase for uniformity

# Step 4: Normalize headers and chunk text by section headers
def chunk_text_by_headers(text):
    headers = [
        "Patient Information", "Introduction", "Medical History", "Presenting Symptoms",
        "Diagnostic Tests Conducted", "Diagnosis", "Treatment Plan", "Medications",
        "Recommendations", "Conclusion", "Discharge Summary", "Prescription", "Blood Test Report"
    ]
    
    # Convert headers to lowercase for consistency with cleaned text
    headers = [header.lower() for header in headers]

    # Case-insensitive regex matching for headers
    pattern = r"(?<=\n)("+ "|".join([re.escape(header) for header in headers]) + r")\s*(?=\n)"
    
    # Split the text based on the headers
    chunks = re.split(pattern, text)
    
    # Clean up the resulting chunks by stripping extra spaces
    cleaned_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    
    return cleaned_chunks

# Sentence splitting for more precise classification
def split_into_sentences(text):
    return nltk.tokenize.sent_tokenize(text)
