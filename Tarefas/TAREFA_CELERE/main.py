from fastapi import FastAPI
from pydantic import BaseModel
from celery_app import calcular_soma, calcular_fatorial 

app = FastAPI(title="API Assíncrona com Celery")

class SomaRequest(BaseModel):
    a: int
    b: int

class FatorialRequest(BaseModel):
    n: int

@app.post("/soma")
def endpoint_soma(dados: SomaRequest):
    tarefa = calcular_soma.delay(dados.a, dados.b)

    return {
        "message": "Tarefa de soma enviada para processamento em background.",
        "task.id": tarefa.id
    }

@app.post("/fatorial")
def endpoint_fatorial(dados: FatorialRequest):
    tarefa = calcular_fatorial.delay(dados.n)

    return {
        "message": "Tarefa de fatorial enviada para processamento em background.",
        "task.id": tarefa.id
    }