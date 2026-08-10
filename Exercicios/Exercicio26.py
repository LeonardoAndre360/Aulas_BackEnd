# Existem n montanhas seguidas e cada montanha tem uma altura.
# Você recebe uma altura de array inteiro, onde altura[i] representa a altura da montanha i e um numero_aleatório inteiro.
# Uma montanha é chamada estável se a montanha imediatamente anterior a ela (se ixistir) tiver uma altura estritamente maior que o limite.
# Observe que a montanha 0 não é estável.
# Retorna um array contendo os índices de todas as montanhas estáveis em qualquer ordem.

alturas_das_montanhas = [1,2,3,4,5]
numero_aleatorio = 2
meu_arrayzinho_resultado = []


for posicao in range(1, len(alturas_das_montanhas)):
    if alturas_das_montanhas[posicao - 1] > numero_aleatorio:
        meu_arrayzinho_resultado.append(posicao - 1)


print(meu_arrayzinho_resultado)