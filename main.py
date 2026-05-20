from fastapi import FastAPI
import os

app = FastAPI(title="FastAPI com Docker e Poetry")

@app.get("/")
def read_root():
    # Lendo uma variável de ambiente para validar o requisito do exercício
    ambiente = os.getenv("AMBIENTE", "Desenvolvimento")
    return {
        "status": "Rodando",
        "container": "FastAPI + Docker + Poetry",
        "ambiente": ambiente
    }