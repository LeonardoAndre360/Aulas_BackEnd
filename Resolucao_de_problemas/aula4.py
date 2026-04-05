# - Tabuada: Receba um número e exiba a tabuada de 1 a 10 para ele.

# 1. Receber o número para poder mostrar sua tabuada

numero_tabuada = float(input())

# 2. Criar a lógica para mostrar a tabuada

for i in range(1,11):
    print(numero_tabuada * i)