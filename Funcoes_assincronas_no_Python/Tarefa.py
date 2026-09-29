import asyncio
import random
import time

lista_Kanto = ["Bulbassauro", "Charmander", "Squirtle"]
lista_Johto = ["Chikorita", "Cyndaquil", "Totodile"]
lista_Hoenn = ["Treeko", "Torchic", "Mudkip"]

async def busca_kanto():
    print("Procurando pokemon em Kanto...")
    try:
        tempo_espera = random.uniform(1,5)
        await asyncio.sleep(tempo_espera)
        pokemon_encontrado = random.choice(lista_Kanto)

        return pokemon_encontrado, tempo_espera
    except Exception as erro:
        print(f"Erro ao buscar em Kanto: {erro}")
        return "Nenhum", 0

async def busca_johto():
    print("Procurando pokemon em Johto...")
    try:
        tempo_espera = random.uniform(1,5)
        await asyncio.sleep(tempo_espera)
        pokemon_encontrado = random.choice(lista_Johto)

        return pokemon_encontrado, tempo_espera
    except Exception as erro:
            print(f"Erro ao buscar em Johto: {erro}")
            return "Nenhum", 0

async def busca_hoenn():
    print("Procurando pokemon em Hoenn...")
    try:
        tempo_espera = random.uniform(1,5)
        await asyncio.sleep(tempo_espera)
        pokemon_encontrado = random.choice(lista_Hoenn)

        return pokemon_encontrado, tempo_espera
    except Exception as erro:
            print(f"Erro ao buscar em Hoenn: {erro}")
            return "Nenhum", 0

async def main():
    print("Iniciando a busca simultânea pelas 3 regiões...\n")

    tempo_inicio = time.perf_counter()

    resultados = await asyncio.gather(busca_kanto(), busca_johto(), busca_hoenn())

    tempo_fim = time.perf_counter()
    
    tempo_total = (tempo_fim - tempo_inicio)

    print("\n--- Resultado da Busca ---")
    
    pokemon_kanto, tempo_kanto = resultados[0]
    pokemon_johto, tempo_johto = resultados[1]
    pokemon_hoenn, tempo_hoenn = resultados[2]
    
    print(f"Kanto: {pokemon_kanto} (Demorou {tempo_kanto:.2f} segundos)")
    print(f"Johto: {pokemon_johto} (Demorou {tempo_johto:.2f} segundos)")
    print(f"Hoenn: {pokemon_hoenn} (Demorou {tempo_hoenn:.2f} segundos)")
    
    print("--------------------------")
    print(f"Tempo TOTAL de execução: {tempo_total:.2f} segundos")

asyncio.run(main())