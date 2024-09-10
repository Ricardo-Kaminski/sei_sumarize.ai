from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def process_pdfs(file_list):
    texts = {}
    for file_path in file_list:
        text = extract_text_from_pdf(file_path)
        texts[file_path] = text
    return texts
