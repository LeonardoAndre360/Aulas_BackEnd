# Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# 1. Preciso receber esses números separadamente

numero1, numero2, numero3 = map(int, input().split())

# 2. Criar uma lógica para ver quem é o segundo maior 

meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)
meu_array.append(numero3)

meu_array.sort()

# 3. Mostrar na tela quem é o vencer, ou seja, quem é o segundo maior 

print("O segundo maior é:", meu_array[1])