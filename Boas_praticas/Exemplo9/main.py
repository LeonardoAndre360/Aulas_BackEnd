from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
# FastAPI: Cria uma instância do aplicativo FastAPI para definir rotas e lógica de autenticação
security = HTTPBasic()
# HTTPBasic: Configura a autenticação básica para proteger endpoints

def autenticar_meu_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "user"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Credenciais incorretas")
    return credentials.username
# autenticar_meu_usuario: Função que valida as credenciais fornecidas pelo usuário. 
# Se as credenciais estiverem incorretas uma exceção HTTP 401 é levantada

@app.get("/protegido")
def endpoint_protegido(username: str = Depends(autenticar_meu_usuario)):
    return {"message": f"Olá, {username}. Você acessou um endpoint protegido!"} 
# @app.get("/protegido"): Define um endpoint protegido que requer autenticação. 
# Se as credenciais forem válidas, uma mensagem de boas-vindas é retornada