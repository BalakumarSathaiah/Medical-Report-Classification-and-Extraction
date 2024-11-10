import os
from data_extraction import extract_text_from_pdf, extract_tables_from_pdf_with_pdfplumber
from text_processing import clean_text, chunk_text_by_headers
from classification import classify_text, merge_similar_sections

# Function to get file input from user
def get_pdf_path_from_user():
    # Prompt the user to input the file path
    pdf_path = input("Please enter the path to the PDF file: ").strip()

    # Check if the file exists
    if not os.path.isfile(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist. Please check the file path.")
        return None
    
    return pdf_path

# Main function to process PDF
def classify_and_extract_from_pdf(pdf_path):
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("No text extracted. Exiting.")
        return

    print("Cleaning text...")
    cleaned_text = clean_text(text)

    print("Chunking text into sections...")
    text_chunks = chunk_text_by_headers(cleaned_text)

    # Ensure that candidate labels include all possible sections
    candidate_labels = [
        "Patient Information", "Introduction", "Medical History", "Presenting Symptoms",
        "Diagnostic Tests", "Diagnosis", "Treatment Plan", "Medications",
        "Recommendations", "Conclusion", "Discharge Summary", "Prescription", "Blood Test Report"
    ]

    formatted_output = []
    for chunk in text_chunks:
        classification_results = classify_text(chunk, candidate_labels)
        formatted_output.extend(classification_results)

    merged_output = merge_similar_sections(formatted_output)

    # Output final merged result
    print("\n".join(merged_output))


# Run the main function
pdf_path = get_pdf_path_from_user()
if pdf_path:
    classify_and_extract_from_pdf(pdf_path)
