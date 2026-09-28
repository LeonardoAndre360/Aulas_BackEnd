import asyncio
import random
import time

lista_Kanto = ["Bulbassauro", "Charmander", "Squirtle"]
lista_Johto = ["Chikorita", "Cyndaquil", "Totodile"]
lista_Hoenn = ["Treeko", "Torchic", "Mudkip"]

async def busca_kanto():
    print("Procurando pokemon em Kanto...")

    tempo_espera = random.uniform(1,5)

    await asyncio.sleep(tempo_espera)

    pokemon_encontrado = random.choice(lista_Kanto)

    return pokemon_encontrado

async def busca_johto():
    print("Procurando pokemon em Johto...")

    tempo_espera = random.uniform(1,5)

    await asyncio.sleep(tempo_espera)

    pokemon_encontrado = random.choice(lista_Johto)

    return pokemon_encontrado

async def busca_hoenn():
    print("Procurando pokemon em Hoenn...")

    tempo_espera = random.uniform(1,5)

    await asyncio.sleep(tempo_espera)

    pokemon_encontrado = random.choice(lista_Hoenn)

    return pokemon_encontrado

async def main():
    print("Iniciando a busca simultânea pelas 3 regiões...\n")

    tempo_inicio = time.perf_counter()

    resultados = await asyncio.gather(busca_kanto(), busca_johto(), busca_hoenn())

    tempo_fim = time.perf_counter()
    
    tempo_total = (tempo_fim - tempo_inicio)

    print(f"Busca concluida")
    print(f"O resultado de Kanto é: {resultados[0]}\n O Resutaldo de Johto é: {resultados[1]}\n O resultado de Hoenn é {resultados[2]}")
    print(f"Tempo total: {tempo_total:.2f} segundos")

asyncio.run(main())