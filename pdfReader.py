import os
from pypdf import PdfReader

#Function to read each pages extract them and store in a array

def read_pdf(pdf_path):
    if not os.path.exists(pdf_path):
       raise FileNotFoundError(f"The file {pdf_path} does not exist")
    
    reader=PdfReader(pdf_path)
    pages=[page.extract_text() for page in reader.pages]  #An array consisting of pages in a pdf
    return pages


