# Na cidade de Digitville, havia uma lista de números chamados meu_arrayzinho contendo números inteiros de 0 a n - 1.
# Cada número deveria aparecer exatamente uma vez na lista.
# No entanto, dois números maliciosos apareceram sorrateiramente, tornando a lista mais longa do que o habitual.
# Como detetive da cidade, sua tarefa é encontrar esses dois números sorrateiros.
# Retorne um array de tamanho dois contendo os dois números (em qualquer ordem), para que a paz possa retornar a Digitville.


meu_arrayzinho = [1,2,3,4,5,5,6,7,8,9,9]

# Chave - Valor

# Número dentro do Array sendo a Chave
# A quantidade de vezes que esse número apareceu sendo o Valor

meu_dicionariozinho = {}

for numero in meu_arrayzinho:
    if numero not in meu_dicionariozinho:
        meu_dicionariozinho[numero] = 1
    else:
        meu_dicionariozinho[numero] += 1

meu_arrayzinho_resultado = []

for chave, valor in meu_dicionariozinho.items():
    if valor == 2:
        meu_arrayzinho_resultado.append(chave)

print(meu_arrayzinho_resultado)