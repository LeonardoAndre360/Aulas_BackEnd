from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import asyncio
import redis.asyncio as redis
import json

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class Livro(BaseModel):
    id_livro: int
    titulo_livro: str
    autor_livro: str

livros_db = []

async def salvar_livros_redis(livros: list):
    livros_dict = [livro.model_dump() for livro in livros]
    livros_json = json.dumps(livros_dict)
    await redis_client.set("livros", livros_json, ex=60)
    print("Cache de livros salvo no Redis.")

async def deletar_livros_redis(livros: list):
    await redis_client.delete("livros")
    print("Cache de livros deletado do Redis.")

@app.get("/livros")
async def listar_livro():

    livros_cache = await redis_client.get("livros")
    if livros_cache:
        print("Encontrado no Cache! Retornando rápido...")
        return json.loads(livros_cache)
    print("Cache Miss! Procurando Livro no banco original...")
    await asyncio.sleep(0.5)
    await salvar_livros_redis(livros_db)
    return livros_db

@app.post("/livros", status_code=status.HTTP_201_CREATED)
async def criar_livro(novo_livro: Livro):
    print("Adicionando Livro...")
    await asyncio.sleep(0.5)
    livros_db.append(novo_livro)
    await deletar_livros_redis(livros_db)
    return novo_livro

@app.put("/livros/{id_livro}")
async def atualizar_livro(id_livro: int, livro_atualizado: Livro):
    print("Atualizando Livro...")
    await asyncio.sleep(0.5)

    for index, livro in enumerate(livros_db):
        if livro.id_livro == id_livro:
            livros_db[index] = livro_atualizado
            await deletar_livros_redis(livros_db)
            return livro_atualizado

    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{id_livro}")
async def deletar_livro(id_livro: int):
    print("Deletando Livro...")
    await asyncio.sleep(0.5)

    for index, livro in enumerate(livros_db):
        if livro.id_livro == id_livro:
            del livros_db[index]
            await deletar_livros_redis(livros_db)
            return{"mensagem": "Livro deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Livro não encontrado")