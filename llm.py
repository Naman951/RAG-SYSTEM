from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API"),
    model_name="llama-3.1-8b-instant"
)

if __name__ == "__main__":
    response = llm.invoke("who was the first president of the united states?")
    print(response.content)



