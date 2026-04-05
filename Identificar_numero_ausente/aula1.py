# Dado um array meu_arrayzinho contendo n números distintos no intervalo [0, n].
# retorne o único número no intervalo que está faltando no array.


meu_arrayzinho = [0,2,3,4,5,6,7,8,9,10]

tamanho_meu_arrayzinho = len(meu_arrayzinho)
soma_valores_meu_arrayzinho = sum(meu_arrayzinho)

soma_total = tamanho_meu_arrayzinho * (tamanho_meu_arrayzinho + 1) // 2

print(soma_total - soma_valores_meu_arrayzinho)