import asyncio

async def pikachu():
    print("Pikachu entrou na arena!")
    await asyncio.sleep(2)
    print("Pikachu usou choque do trovão")
    
async def charmander():
    print("Charmander entrou na arena!")
    await asyncio.sleep(1)
    print("Charmander usou brasas!")
    
async def batalha():
    await asyncio.gather(pikachu(), charmander())

asyncio.run(batalha())

# asyncio = Ferramenta que iremos usar para criar processos assincronos
# async = Palavra reservada para definir que aquela função vai ser uma função assíncrona
# await = Palavra reservada para definir qual processo deverar ser o processp assíncrono
    
