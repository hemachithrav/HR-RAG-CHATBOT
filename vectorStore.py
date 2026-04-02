from pinecone import Pinecone
import os
from dotenv import load_dotenv
from typing import List

# Load environment variables
load_dotenv(dotenv_path=".env")

#Initialize Pincecone CLient

pinecone_Client= Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index=pinecone_Client.Index(os.getenv('PINECODE_INDEX_NAME'))

"""
👉 Pinecone expects data in this format:

{
  "id": "unique_id",
  "values": [vector numbers],
  "metadata": {extra info}
}
🔍 Line-by-line explanation
🟢 Function definition
def store_in_pinecone(chunks, embeddings, namespace=""):

👉 Inputs:

chunks → your text pieces
embeddings → vectors for each chunk
namespace → optional grouping

🟢 Empty list
vectors_to_upsert = []

👉 This will store all vectors before sending to Pinecone

🟢 Loop through chunks + embeddings
for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

👉 What happens:

zip() → pairs chunk + embedding
enumerate() → gives index i   (--->)

Example:

chunk_0 → text + vector  
chunk_1 → text + vector  

🟢 Create vector data
vector_data = {
    "id": f"chunk_{i}",

👉 Unique ID for each chunk
Example:

chunk_0, chunk_1, chunk_2
"values": embedding,

👉 This is your vector (numbers)
👉 Example:

[0.12, -0.45, 0.88, ...]
"metadata": {
    "text": chunk,
    "chunk_index": i
}

"""

def store_in_pinecone(chunks:List[str],embeddings:List[List[float]], namespace:str=""):
    vectors_to_upsert=[]
    for i,(chunk,embedding) in enumerate(zip(chunks,embeddings)):
        vector_data={
            "id": f"chunk_{i}",
            "values":embedding,
            "metadata":{
                "text":chunk,
                "chunk_index":i
            }
        }
        vectors_to_upsert.append(vector_data)


# Upsert Vectors in batches

    batch_size=100
    for i in range(0,len(vectors_to_upsert),batch_size):  #length and jump 100 as batch size
        batch=vectors_to_upsert[i:i+batch_size] #first 100 batch next 100
        print(f"Uploading batch {i} to {i+len(batch)}")
        
        index.upsert(vectors=batch,namespace=namespace)    #upload in pinecone



def search_in_pinecone(query_vector:List[float],top_k:int=4,namespace:str=""):
    results=index.query(
            vector=query_vector,          
            top_k=top_k,
            include_metadata=True,
            namespace=namespace
    )
    print(f"Found {len(results.matches)} matches for the query")
    matched_chunks=[]
    for match in results.matches:
        matched_chunks.append(match.metadata.get("text",""))
    return matched_chunks


