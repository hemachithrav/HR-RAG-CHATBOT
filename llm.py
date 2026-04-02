from google import genai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

# Configure Gemini
#api_key = os.getenv("GEMINI_API_KEY")


api_key = os.getenv("GEMINI_API_KEY")

# Proper client initialization

client=genai.Client(api_key=api_key)
"""
models = client.models.list()
for m in models:
    print(m.name, m.supported_actions)

"""
def query_llm_with_context(query:str, context:str):

       # limit chunks

    system_content = """
    You are a helpful assistant for answering user queries based on provided context. 
    Use the context to provide accurate and relevant answers.
    Do not make assumptions beyond the context provided. 
    If the context does not contain enough information to answer the query, 
    let the user know that you cannot provide an answer based on the given context..

    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",   # ✅ important change
        contents=system_content,
        config={"temperature": 0.4}
    )

    try:
        return response.text
    except (IndexError, AttributeError):
        return "Error: Could not extract response text from the model."


