from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Documentos de exemplo. Você pode trocar por sua base!
DOCUMENTOS = [
    "O céu é azul.",
    "A água é essencial para a vida.",
    "A inteligência artificial está mudando o mundo.",
    "Python é uma linguagem muito utilizada em IA.",
    "A AWS Lambda permite rodar código serverless.",
    "O LangChain facilita a integração com LLMs e bancos vetoriais."
]


def criar_db():
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(DOCUMENTOS, embeddings)
    return db

def buscar_vetorial(pergunta, top_k=3):
    db = criar_db()
    resultados = db.similarity_search(pergunta, k=top_k)
    return [r.page_content for r in resultados]