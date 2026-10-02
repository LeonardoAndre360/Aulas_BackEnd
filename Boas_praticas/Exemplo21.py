from celery import Celery
# Celery: Importa a classe Celery, que é usada para criar uma instância de aplicação Celery.

# Configuração do Celery com o broker Redis
app = Celery('tasks', broker='redis://localhost:6379/0')
# app = Celery('tasks', broker='redis://localhost:6379/0'): 
# Configura o Celery para usar o Redis como broker, que gerencia a fila de mensagens.

@app.task
def add(x, y):
    return x + y
# @app.task: Define a função add como uma tarefa Celery, que pode ser executada de forma assíncrona.

# Executar a tarefa
result = add.delay(4, 6)
# add.delay(4, 6): Executa a tarefa add de forma assíncrona, passando os argumentos 4 e 6.
print('Task result:', result.get())
# result.get(): Obtém o resultado da tarefa assíncrona após sua conclusão.

