# API de Gerenciamento de Livros (Assíncrona com Redis)

Esta é uma API construída com FastAPI para praticar os conceitos de concorrência, processamento assíncrono (async/await) e otimização de performance aplicando a estratégia de cache-aside com Redis.

## Como rodar o projeto

### 1. Configurar e iniciar o Redis (via Docker)
Para que o cache da aplicação funcione, inicie um container do Redis localmente mapeando a porta padrão. No terminal, execute:
`docker run -d -p 6379:6379 --name redis_cache redis:alpine`

### 2. Instalar as dependências necessárias
Certifique-se de instalar as ferramentas essenciais para rodar e conectar a API ao Redis. Utilizando o Poetry ou o pip:
`poetry add fastapi uvicorn redis`
*(Ou `pip install fastapi uvicorn redis`)*

### 3. Executar o servidor do FastAPI
Inicie a aplicação utilizando o Uvicorn:
`uvicorn Tarefa2_Redis:app --reload` 

### 4. Acessar a documentação interativa
Abra o navegador e acesse a documentação do Swagger UI para testar os endpoints:
`http://127.0.0.1:8000/docs`

---

## Evidências de Teste (CURL)

Abaixo estão os comandos reproduzíveis utilizando `curl` para testar cada cenário da API. 

### 1. Adicionar novos mangás (POST) - Sucesso (Status 201)

**Comando (Shingeki no Kyojin):**
`curl -X 'POST' 'http://127.0.0.1:8000/livros' -H 'Content-Type: application/json' -d '{"id_livro": 1, "titulo_livro": "Shingeki no Kyojin", "autor_livro": "Hajime Isayama"}'`

**Comando (Jujutsu Kaisen):**
`curl -X 'POST' 'http://127.0.0.1:8000/livros' -H 'Content-Type: application/json' -d '{"id_livro": 2, "titulo_livro": "Jujutsu Kaisen", "autor_livro": "Gege Akutami"}'`

**Comando (Dragon Ball):**
`curl -X 'POST' 'http://127.0.0.1:8000/livros' -H 'Content-Type: application/json' -d '{"id_livro": 3, "titulo_livro": "Dragon Ball", "autor_livro": "Akira Toriyama"}'`

**Comando (Yu-Gi-Oh!):**
`curl -X 'POST' 'http://127.0.0.1:8000/livros' -H 'Content-Type: application/json' -d '{"id_livro": 4, "titulo_livro": "Yu-Gi-Oh!", "autor_livro": "Kazuki Takahashi"}'`

### 2. Listar a coleção (GET) - Sucesso (Status 200)

> **Nota sobre o Cache:** Ao executar o endpoint GET pela primeira vez, o tempo de resposta refletirá uma busca no banco original (*Cache Miss*). Execuções imediatamente posteriores retornarão a resposta instantaneamente a partir da memória (*Cache Hit*).

**Comando:**
`curl -X 'GET' 'http://127.0.0.1:8000/livros'`

**Retorno Esperado:**
`[{"id_livro": 1, "titulo_livro": "Shingeki no Kyojin", "autor_livro": "Hajime Isayama"}, {"id_livro": 2, "titulo_livro": "Jujutsu Kaisen", "autor_livro": "Gege Akutami"}, {"id_livro": 3, "titulo_livro": "Dragon Ball", "autor_livro": "Akira Toriyama"}, {"id_livro": 4, "titulo_livro": "Yu-Gi-Oh!", "autor_livro": "Kazuki Takahashi"}]`

### 3. Atualizar um volume específico (PUT) - Sucesso (Status 200)

*Exemplo: Atualizando o título para especificar um arco narrativo. Esta operação invalida o cache atual.*

**Comando:**
`curl -X 'PUT' 'http://127.0.0.1:8000/livros/2' -H 'Content-Type: application/json' -d '{"id_livro": 2, "titulo_livro": "Jujutsu Kaisen - Culling Game", "autor_livro": "Gege Akutami"}'`

**Retorno Esperado:**
`{"id_livro": 2, "titulo_livro": "Jujutsu Kaisen - Culling Game", "autor_livro": "Gege Akutami"}`

### 4. Atualizar um mangá inexistente (PUT) - Erro (Status 404)

**Comando:**
`curl -X 'PUT' 'http://127.0.0.1:8000/livros/99' -H 'Content-Type: application/json' -d '{"id_livro": 99, "titulo_livro": "Hunter x Hunter", "autor_livro": "Yoshihiro Togashi"}'`

**Retorno Esperado:**
`{"detail": "Livro não encontrado"}`

### 5. Deletar um mangá (DELETE) - Sucesso (Status 200)

*Exemplo: Esta operação invalida o cache atual para não retornar dados fantasmas nas próximas listagens.*

**Comando:**
`curl -X 'DELETE' 'http://127.0.0.1:8000/livros/4'`

**Retorno Esperado:**
`{"mensagem": "Livro deletado com sucesso!"}`

### 6. Deletar um mangá inexistente (DELETE) - Erro (Status 404)

**Comando:**
`curl -X 'DELETE' 'http://127.0.0.1:8000/livros/99'`

**Retorno Esperado:**
`{"detail": "Livro não encontrado"}`