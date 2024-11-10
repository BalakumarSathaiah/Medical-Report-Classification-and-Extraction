# Medical-Report-Classification-and-Extraction

This project is designed to automatically extract and classify sections from medical PDF reports, helping to streamline the process of handling unstructured medical data. It uses Natural Language Processing (NLP) techniques to extract key sections and classify them into predefined categories with high accuracy.

## Key Features
- **PDF Text Extraction**: Uses `pdfplumber` to extract text from multi-page PDF reports, handling both text and table extraction.
- **Text Cleaning**: Cleans and normalizes the extracted text for uniformity (e.g., removes extra spaces, converts text to lowercase).
- **Section Chunking**: Splits text into sections based on predefined headers (e.g., "Patient Information", "Diagnosis").
- **Zero-Shot Classification**: Classifies text sections and sentences into predefined categories using Hugging Face's `facebook/bart-large-mnli` model without requiring task-specific training.
- **Overlapping Section Merging**: Merges repeated or overlapping sections (e.g., "Patient Information") based on the highest confidence score to ensure accurate output.
- **Confidence Scoring**: Outputs classified sections with confidence scores, helping assess the reliability of the classifications.

## Technologies Used
- **Text Extraction**: `pdfplumber` for extracting text and tables from PDFs.
- **Text Processing**:
  - `re` (Regular Expressions) for cleaning and chunking text based on section headers.
  - `nltk` for sentence tokenization to improve classification granularity.
- **Classification**: Hugging Face's `transformers` library to apply a pre-trained zero-shot classification model (`facebook/bart-large-mnli`).

## Step-by-Step Logic
1. **PDF Text Extraction**
   - The program first extracts text from the provided PDF using `pdfplumber`, retrieving both structured (tables) and unstructured text for processing.

2. **Text Cleaning**
   - Extracted text is cleaned:
     - Multiple spaces are reduced to a single space.
     - Text is converted to lowercase to ensure uniformity.

3. **Chunking Text by Headers**
   - The cleaned text is split into chunks based on predefined section headers (e.g., "Patient Information", "Diagnosis").
   - Each section is treated individually for classification.

4. **Sentence-Level Classification**
   - The text within each section is further split into sentences using `nltk` sentence tokenizer, improving classification accuracy by focusing on smaller pieces of content.

5. **Zero-Shot Classification**
   - A pre-trained zero-shot classification model (`facebook/bart-large-mnli`) is applied to classify each sentence into one of the predefined labels:
     - "Patient Information"
     - "Introduction"
     - "Medical History"
     - "Presenting Symptoms"
     - "Diagnosis"
     - "Treatment Plan"
     - "Medications"
     - "Recommendations"
     - "Conclusion"
     - "Discharge Summary"
     - "Prescription"
     - "Blood Test Report"
   - Each sentence is classified with a confidence score, indicating the model's certainty in its classification.

6. **Merging Overlapping Sections**
   - If the same section appears multiple times (e.g., "Patient Information" in different chunks), the content is merged based on the highest classification confidence. This avoids duplication and ensures cohesive output.

7. **Output**
   - The final output includes each classified section with its corresponding label and confidence score. Overlapping sections are merged for clarity and completeness, presenting the output in a clear, easy-to-read format.

## Expected Output
**Input**: A medical report in PDF format containing sections like:
   - Patient Information
   - Medical History
   - Presenting Symptoms

**Output**:
```plaintext
Patient Information - Patient Information (Confidence: 0.82)
Content: Name: Emily Johnson, Date of Birth: 01/15/1989, Patient ID: 987654321, etc.

Medical History - Medical History (Confidence: 0.59)
Content: medical history: ms. johnson has a history of hypertension, diagnosed three years ago, which she has been managing with medication.

Presenting Symptoms - Presenting Symptoms (Confidence: 0.57)
Content: presenting complaints: ms. johnson presented with intermittent chest pain,...

```
## Section Labeling and Confidence Scoring
- Each section is clearly labeled with its classification label and confidence score.
- Overlapping sections (e.g., multiple mentions of "Patient Information") are merged for clarity and completeness.

## Usage Instructions
1. **Prepare Your PDF File**  
   Ensure your medical report is in PDF format.

2. **Run the Script**  
   In the terminal, run:
   ```bash
   python main.py

3. **Provide the PDF Path**  
   Enter the path to your PDF file when prompted.

4. **View the Output**  
   The classified and extracted sections will be displayed in the terminal, with each section's content and confidence score.


