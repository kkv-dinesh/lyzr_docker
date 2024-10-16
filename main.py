import os
from fastapi import FastAPI
from lyzr import QABot
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_api_key

app = FastAPI()

pdf_path = "data/KME_Products.pdf"
my_chatbot = QABot.pdf_qa(input_files=[pdf_path])

@app.post("/query")
async def query_pdf(query: str):
    response = my_chatbot.query(query)
    return {"query": query, "response": response}
