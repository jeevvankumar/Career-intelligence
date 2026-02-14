import pdfplumber

def extract_text_from_pdf(uploaded_file):
    resume_text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text()
    return resume_text.lower()
