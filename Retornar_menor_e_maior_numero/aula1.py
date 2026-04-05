# Dada um array de números inteiros, retorne a soma do menor número e do maior número do array

meu_arrayzinho = [1,5,33,8,77,43,124,6,8,99]

# 1. Vamos ordernar o array para poder deixar o menor valor na posição zero do array
# e o maior valor na última posição do array

meu_arrayzinho.sort()

# 2. Efetuar a soma do valor que está na ultima posição ao valor que está na primeira posição 

primeiro_valor = meu_arrayzinho[0]
ultimo_valor = meu_arrayzinho[-1]

print(primeiro_valor + ultimo_valor)