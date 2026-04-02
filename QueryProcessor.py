from Embedder import embeded_query
from vectorStore import search_in_pinecone
from llm import query_llm_with_context
from typing import List

def process_user_query(query:str):


#Embed the user's query to create a vector representation
    query_vector=embeded_query(query)

# Search the Vector DB(Pinecone DB) TO find top matching chunks related to User questions
    matched_chunks=search_in_pinecone(query_vector)
    print("Matched chunks:", matched_chunks)

#Send the user query and search results(query+context) to the LLM for generating response
    generated_response=query_llm_with_context(query,matched_chunks)

    print(generated_response)

   



if __name__=="__main__":
    user_query="Give me about sexual harrasment policy"
    process_user_query(user_query)