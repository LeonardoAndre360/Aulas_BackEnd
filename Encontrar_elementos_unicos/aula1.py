# Dada um array números de inteiros, cada elemento aparece duas vezes, exceto um. Encontre aquele únicos.

meu_arrayzinho = [1,1,2,2,3,3,4,5,5,5,6,6]

# 1. Criar um dicionario para adicionar os valores do array através de chave - valor
# ou seja, a chave sendo o valor do array e o valor sendo a quantidade de vezes que a chave apareça

meu_dicionariozinho = {}

for i in meu_arrayzinho:
    if  i not in meu_dicionariozinho:
        meu_dicionariozinho[i] = 1
    else:
        meu_dicionariozinho[i] += 1


# 2. Fazer a verificação de qual valor aparece apenas uma vez

for chave, valor in meu_dicionariozinho.items():
    if valor == 1:
        print(chave)