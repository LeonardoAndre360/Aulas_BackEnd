# Receba um número e determine se ele é um palídromo (lê-se igual e frente para trás)

# 1. Receber um número inteiro

meu_numero = int(input())

# 2. Determinar se é um palindromo
# 3. Retronar se é ou não é
minha_string = str(meu_numero)

if minha_string == minha_string[::-1]:
    print("É um palindromo")
else:
    print("Não é um palindromo")

