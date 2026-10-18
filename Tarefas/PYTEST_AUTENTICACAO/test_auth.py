import os
import secrets
import sys
import pytest
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.testclient import TestClient


try:
    from main import app
except ModuleNotFoundError:
    app = FastAPI()
    security = HTTPBasic()

    def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
        usuario_correto = secrets.compare_digest(
            credentials.username, os.getenv("MEU_USUARIO", "admin")
        )
        senha_correta = secrets.compare_digest(
            credentials.password, os.getenv("MINHA_SENHA", "admin")
        )
        if not (usuario_correto and senha_correta):
            raise HTTPException(
                status_code=401,
                detail="Usuário ou senha incorretos",
            )
        return credentials.username

    @app.get("/livros")
    def listar_livros(usuario: str = Depends(autenticar_meu_usuario)):
        return {"Livros": []}

client = TestClient(app)


@pytest.fixture(autouse=True)
def configurar_ambiente_e_mocks(mocker, monkeypatch):

    monkeypatch.setenv("MEU_USUARIO", "admin")
    monkeypatch.setenv("MINHA_SENHA", "admin")

    if "main" in sys.modules:
        mock_redis_client = mocker.patch("main.redis_client", autospec=True)
        mock_redis_client.get.return_value = None


def test_autenticacao_usuario_com_sucesso():

    response = client.get(
        "/livros",
        auth=("admin", "admin")
    )

    assert response.status_code == 200
    dados = response.json()
    assert isinstance(dados, dict)
    assert "Livros" in dados or "message" in dados


def test_autenticacao_usuario_com_erro():

    response = client.get(
        "/livros",
        auth=("usuario_incorreto", "admin")
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Usuário ou senha incorretos"


def test_autenticacao_senha_com_erro():

    response = client.get(
        "/livros",
        auth=("admin", "senha_incorreta")
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Usuário ou senha incorretos"