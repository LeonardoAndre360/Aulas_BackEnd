import asyncio

async def say_hello():
# say_hello: Função assíncrona que imprime "Hello", aguarda um segundo e depois imprime "World". 
# O uso de await permite que outras tarefas sejam executadas durante o tempo de espera.
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())
# main: Função principal que utiliza asyncio.gather para executar duas instâncias de say_hello simultaneamente.


asyncio.run(main())
# asyncio.run(main()): Inicia o Event Loop e executa a função main, 
# demonstrando como o processamento assíncrono permite a execução de múltiplas tarefas de forma eficiente.