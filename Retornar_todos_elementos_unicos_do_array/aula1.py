# Você recebe um array de números inteiros meu_arrayzinho
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos de meu_arrayzinho

meu_arrayzinho = [1,2,3,3,2,4,5,5,7,6,6]

# 1. Criar um dicionário para adicionar uma chave e valor

meu_dicionariozinho = {}

for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i] = 1
    else:
        meu_dicionariozinho[i] += 1

# 2. Encontrar quem são os valores que aparecem uma única vez
# 3. Fazer a soma das chaves que aparecem apenas 1 vez

soma_das_chaves = 0

for chave, valor in meu_dicionariozinho.items():
    if valor == 1:
        soma_das_chaves += chave


print(soma_das_chaves)