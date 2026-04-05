# dado um array de inteiros meu_arrayzinho, um inteiro sortudo é um inteiro que tem uma frequência no array igual ao seu valor

meu_arrayzinho = [1,2,3,3,4,4,5,6,7,1,2]


# 1. Criar um dicionario para adicionar todos os valores, descobrindo, assim, as chaves e valores
# A chave é o próprio número e o valor é a frequência (ou seja, a quantidade de vezes que este número apareceu no array)

meu_dicionariozinho = {}

for i in meu_arrayzinho:
    if i not in meu_dicionariozinho:
        meu_dicionariozinho[i] = 1
    else:
        meu_dicionariozinho[i] += 1

print(meu_dicionariozinho)

# 2. Fazer um loop dentro do meu dicionário e descobrir quem é a chave que é igual ao valor

for chave, valor in meu_dicionariozinho.items():
    if chave == valor:
        print(chave)
