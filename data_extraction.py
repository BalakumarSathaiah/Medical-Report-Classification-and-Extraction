import pdfplumber

# Step 1: Extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"  # Extract text from each page
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

# Step 2: Extract tables using pdfplumber (optional for tables)
def extract_tables_from_pdf_with_pdfplumber(pdf_path):
    tables = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                tables.extend(page_tables)
    except Exception as e:
        print(f"Error extracting tables from PDF: {e}")
    return tables
