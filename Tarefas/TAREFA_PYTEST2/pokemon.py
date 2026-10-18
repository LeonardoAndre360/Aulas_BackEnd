def calcula_pontos_ataque(pokemon: dict) -> int:
    """
    Calcula os pontos de ataque de um Pokémon.
    Recebe um dicionário com os dados do Pokémon e retorna um número inteiro.
    A lógica matemática consiste em multiplicar a força base pelo nível atual.    
    
    """
    return pokemon["forca_base"] * pokemon["nivel"]

def pokemon_evolui(pokemon: dict, nivel_evolucao: int) -> bool:
    """
    Verifica se o Pokémon atinge o nível mínimo exigido para evoluir.
    Recebe o dicionário do Pokémon e um número inteiro representando o nível alvo.
    Retorna True (Verdadeiro) se puder evoluir, ou False (Falso) caso contrário.

    Retorna True se o Pokémon pode evoluir.
    """
    return pokemon["nivel"] >= nivel_evolucao