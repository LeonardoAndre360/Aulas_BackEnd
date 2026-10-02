# API Assíncrona com Celery e Redis

Este projeto demonstra a integração de uma API desenvolvida em FastAPI com o Celery, utilizando o Redis como broker de mensagens e backend de resultados. O objetivo é simular e gerir tarefas pesadas em background (cálculo de soma e fatorial) sem bloquear as respostas da API, garantindo alta performance e escalabilidade.

## 🛠️ Tecnologias Utilizadas
* **Python 3.14**
* **FastAPI:** Framework web para construção da API.
* **Celery:** Fila de tarefas (Task Queue) para processamento assíncrono.
* **Redis:** Broker de mensagens e armazenador de resultados.
* **Uvicorn:** Servidor ASGI para rodar o FastAPI.

## ⚙️ Pré-requisitos
* Python instalado na máquina.
* Docker instalado e a correr (para disponibilizar a instância do Redis).

## 🚀 Como Instalar e Executar

### Passo 1: Iniciar o Redis via Docker
Abra o seu terminal e execute o seguinte comando para criar e iniciar o contentor do Redis:
```bash
docker run -d -p 6379:6379 --name redis-desafio redis:7-alpine