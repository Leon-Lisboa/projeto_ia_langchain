from fastapi import FastAPI
from pydantic import BaseModel
from .llm_chain import consultar_llm
from .vector_db import buscar_vetorial

from mangum import Mangum  # Para AWS Lambda

app = FastAPI(
    title="API IA com LangChain",
    description="API REST que responde perguntas usando LLMs e busca vetorial.",
    version="1.0"
)

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    # Busca contexto no banco vetorial
    similares = buscar_vetorial(request.question)
    contexto = "\n".join(similares)
    resposta = consultar_llm(request.question, contexto)
    return {
        "question": request.question,
        "context": similares,
        "answer": resposta
    }

# Suporte para AWS Lambda
handler = Mangum(app)