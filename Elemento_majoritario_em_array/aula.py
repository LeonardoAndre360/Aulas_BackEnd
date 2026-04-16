# Dado um array meu_arrayzinho de tamanho n, retorne o elemento majoritário
# O elemento majoritário é aquele que aparece mais de [n/2] vezes.
# Você pode assumir que o elemento majoritário sempre existe no array.

meu_arrayzinho = [3,2,3]
# n é o tamanho do meu_arrayzinho
n = len(meu_arrayzinho)
#item majoritário é o item que aparece mais de n/2 vezes
item_majoritario = n/2

meu_dicionariozinho = {}

for item in meu_arrayzinho:
    if item not in meu_dicionariozinho:
        meu_dicionariozinho[item] = 1
    else:
        meu_dicionariozinho[item] += 1

for chave, valor in meu_dicionariozinho.items():
    if valor >= item_majoritario:
        print(chave)