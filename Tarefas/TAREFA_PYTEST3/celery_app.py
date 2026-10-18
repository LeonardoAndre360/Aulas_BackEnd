from celery import Celery
import os
import time

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_URL = os.getenv("REDIS_URL", f"redis://{REDIS_HOST}:{REDIS_PORT}/0")

celery_app = Celery(
    "Tarefa_Desafio",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery_app.conf.update(
    task_track_started=True,
    result_expires=3600,
    result_serializer="json",
    accept_content=["json"],
)

@celery_app.task(name="calcular_soma")
def calcular_soma(a: int, b: int):
    time.sleep(5)
    return a + b

@celery_app.task(name="calcular_fatorial")
def calcular_fatorial(n: int):
    time.sleep(5)
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado