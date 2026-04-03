# This file sends chunked text to Gemini to convert to vectors

from google import genai
from dotenv import load_dotenv
import os
from typing import List

# Load environment variables
load_dotenv(dotenv_path=".env")

# Debug (check if key is loaded)
# print("KEY:", os.getenv("GEMINI_API_KEY"))

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found. Check your .env file")

client=genai.Client(api_key=api_key)

# Embedding model
EMBEDDING_MODEL = "gemini-embedding-001"

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """Convert text chunks into embeddings using Gemini"""

    embeddings = []

    for chunk in chunks:
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=chunk
        )
        embed_length=response.embeddings[0].values
                # ✅ Print ONLY for first chunk
        if len(embeddings) == 0:
            print("Embedding length:", len(embed_length))
        embeddings.append(embed_length)

       
    return embeddings

#Embeds User query 


    
def embeded_query(query: str) -> List[float]:
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=[query]
    )
    
    embedding = response.embeddings[0].values
    
    # Print the embedding for debugging
    print(f"Query: {query}")
    print(f"Embedding length: {len(embedding)}")
    print(f"Embedding vector (first 10 dims): {embedding[:10]}")  # only first 10 numbers
    
    return embedding
   
    
