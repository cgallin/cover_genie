
from pdfminer.high_level import extract_text

def pdf_to_text(file_path):
    text = extract_text(file_path)
    return text