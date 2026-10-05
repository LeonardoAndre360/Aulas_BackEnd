from pokemon import calcular_pontos_ataque, pokemon_evolui

def test_calcular_pontos_ataque_nivel_um():
    resultado = calcular_pontos_ataque(10, 1)
    assert resultado == 10

def test_calcular_pontos_ataque_nivel_zero():
    resultado = calcular_pontos_ataque(5, 0)
    assert resultado == 0

def test_calcular_pontos_ataque_nivel_cinco():
    resultado = calcular_pontos_ataque(20, 5)
    assert resultado == 100

def test_pokemon_evolui_nivel_atual_menor():
    resultado = pokemon_evolui(15, 20)
    assert resultado == False

def test_pokemon_evolui_nivel_atual_igual():
    resultado = pokemon_evolui(20, 20)
    assert resultado == True

def test_pokemon_evolui_nivel_atual_maior():
    resultado = pokemon_evolui(25, 20)
    assert resultado == True