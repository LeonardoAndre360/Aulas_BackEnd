import pytest
from pokemon import calcula_pontos_ataque, pokemon_evolui

# Fixture: Preparação do ambiente de testes
# O decorador @pytest.fixture é utilizado para criar dados padronizados.
# Isso elimina a repetição de código, permitindo que o mesmo dicionário 
# seja injetado automaticamente em múltiplos testes diferentes.

@pytest.fixture
def bulbasaur():
    """Fixture que cria e retorna os dados pré-configurados do Pokémon Bulbasaur."""
    return {"nome": "Bulbasaur", "forca_base": 49, "nivel": 10}

@pytest.fixture
def charmander():
    """Fixture que cria e retorna os dados pré-configurados do Pokémon Charmander."""
    return {"nome": "Charmander", "forca_base": 52, "nivel": 15}

# Testes Unitarios: calcula_pontos_ataque

def test_calcula_pontos_ataque_bulbasaur(bulbasaur):
    """
    Testa se o cálculo de ataque do Bulbasaur está correto.
    Passo a passo:
    1. O PyTest injeta o dicionário gerado pela fixture 'bulbasaur'.
    2. A função calcula_pontos_ataque executa a matemática (49 * 10).
    3. A instrução 'assert' valida se o resultado real é exatamente 490.
    """
    resultado = calcula_pontos_ataque(bulbasaur)
    assert resultado == 490

def test_calcula_pontos_ataque_charmander(charmander):
    """
    Testa se o cálculo de ataque do Charmander está correto.
    Usa a fixture 'charmander' e garante que a multiplicação de 52 por 15 resulta em 780.
    """
    resultado = calcula_pontos_ataque(charmander)
    assert resultado == 780



# Testes Unitários: pokemon_evolui


def test_pokemon_evolui_charmander(charmander):
    """
    Testa a função de evolução para o Charmander (Nível 15) em dois cenários lógicos.
    O objetivo é garantir que a função lida corretamente com a condição de 'maior ou igual'.
    """
    # Cenário 1: O nível de evolução exigido (20) é MAIOR que o nível atual (15).
    # O teste usa o 'assert' para garantir que a função retorne a recusa (False).
    assert pokemon_evolui(charmander, 20) is False
    
    # Cenário 2: O nível de evolução exigido (15) é IGUAL ao nível atual (15).
    # O teste garante que a função aprova a evolução (True).
    assert pokemon_evolui(charmander, 15) is True

def test_pokemon_evolui_bulbasaur(bulbasaur):
    """
    Testa a função de evolução para o Bulbasaur (Nível 10).
    Verifica a negação quando o requisito é maior (16) e a aprovação quando o nível bate (10).
    """
    # Verifica recusa
    assert pokemon_evolui(bulbasaur, 16) is False
    # Verifica aprovação
    assert pokemon_evolui(bulbasaur, 10) is True