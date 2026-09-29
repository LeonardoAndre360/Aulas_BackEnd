from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

class Livro(BaseModel):
    id_livro: int
    titulo_livro: str
    autor_livro: str

livros_db = []

@app.get("/livros")
async def listar_livro():
    print("Procurando Livro...")
    await asyncio.sleep(0.5)
    return livros_db

@app.post("/livros")
async def criar_livro(novo_livro: Livro):
    print("Adicionando Livro...")
    await asyncio.sleep(0.5)
    livros_db.append(novo_livro)
    return novo_livro

@app.put("/livros/{id_livro}")
async def atualizar_livro(id_livro: int, livro_atualizado: Livro):
    print("Atualizando Livro...")
    await asyncio.sleep(0.5)

    for index, livro in enumerate(livros_db):
        if livro.id_livro == id_livro:
            livros_db[index] = livro_atualizado
            return livro_atualizado

    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{id_livro}")
async def deletar_livro(id_livro: int):
    print("Deletando Livro...")
    await asyncio.sleep(0.5)

    for index, livro in enumerate(livros_db):
        if livro.id_livro == id_livro:
            del livros_db[index]
            return{"mensagem": "Livro deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Livro não encontrado")