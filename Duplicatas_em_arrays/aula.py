# Dado um array inteiro meu_arrayzinho, retorne verdadeiro se algum valor aparecer pelo menos duas vezes no array
# E retorne falso se cada elemento for distinto.

meu_arrayzinho = [1,1,1,3,3,4,3,2,2]

novo_array = sorted(meu_arrayzinho)

meu_dicionariozinho = {}

for numero in novo_array:
    if numero not in meu_dicionariozinho:
        meu_dicionariozinho[numero] = 1
    else:
        meu_dicionariozinho[numero] += 1
        

for chave, valor in meu_dicionariozinho.items():
    if valor >= 2:
        print(True)
    else:
        print(False)