import asyncio

async def fetch_data():
# fetch_data: Função assíncrona que simula a busca de dados com um atraso de 2 segundos, representando uma operação de I/O.
    print("Iniciando a busca de dados...")
    await asyncio.sleep(2) # Simula uma operação de I/O
    print("Dados buscados com sucesso!")
    return {"data": "Exemplo de dados"}

async def main():
    print("Iniciando a aplicação...")
    data = await fetch_data()
    print(f"Dados recebidos: {data}")
# main: Função principal que chama fetch_data e aguarda sua conclusão, imprimindo os dados recebidos.

asyncio.run(main())
# asyncio.run(main()): Executa a função main, iniciando o loop de eventos assíncrono.

# Este exemplo demonstra como usar asyncio para executar tarefas assíncronas em Python, 
# mantendo a aplicação responsiva enquanto aguarda operações de I/O.
