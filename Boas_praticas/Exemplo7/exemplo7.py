from fastapi import FastAPI

app = FastAPI()
# FastAPI(): Cria uma instância do FastAPI, que será usada para definir as rotas da API.

@app.get("/")
async def read_root():
    return {"Hello": "World"}
# @app.get("/"): Define uma rota GET para a raiz do servidor, 
# que retorna um dicionário com a mensagem "Hello World".

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
# @app.get("/items/{item_id}"): Define uma rota GET que aceita um 
# parâmetro item_id na URL e um parâmetro opcional q na query string. 
# Retorna um dicionário com o item_id e o valor de q.

# Este exemplo demonstra como criar rotas básicas usando o FastAPI, 
# permitindo que você comece a construir APIs rapidamente.