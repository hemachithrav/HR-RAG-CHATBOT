# This is the main file which Orchestrates everything.
from pdfReader import read_pdf
from chunker import chunk_pages
from Embedder import embed_chunks
from vectorStore import store_in_pinecone
from typing import List

#Mention pdf Path

pdf_path = 'venv/Resources/HR-Policy.pdf'
def run():

    # 1.Read HR Policy document and extract text

    pages=read_pdf(pdf_path)
    """
    print(f"Extracted {len(pages)} pages from the pdf")
    print("First Page content")
    print(pages[0] if pages else "No content found")
    """
    
    # 2. strip the text into small chunks
    chunks=chunk_pages(pages,chunk_size=900,chunk_overlap=150)

    """
    print(f"Total chunks created:{len(chunks)}")
    print(chunks[0]) #print first chunk

    """
    #3. Embedding
    embeded_chunks=embed_chunks(chunks)
    print(f"Total length of embedded chunks: {len(embeded_chunks)}")
    print(f"First chunk embedding: {embeded_chunks[0]}")


    #4. Store Embedded vectors in Pinecone Database
    store_in_pinecone(chunks,embeded_chunks,namespace='')

    
if __name__=='__main__':
    run()