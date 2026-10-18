from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
# FastAPI: Cria uma aplicação FastAPI com um endpoint que retorna um item com base no item_id e um parâmetro opcional q.

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

client = TestClient(app)
# TestClient: Utilizado para simular requisições HTTP para a aplicação FastAPI, permitindo testar os endpoints.

def test_read_item():
# test_read_item: Função de teste que verifica se o endpoint /items/42?q=fastapi 
# retorna o status code 200 e a resposta JSON esperada.
    response = client.get("/items/42?q=fastapi")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "fastapi"}

# Este exemplo demonstra como o TDD pode ser aplicado para garantir que os endpoints de uma API FastAPI funcionem conforme o esperado.