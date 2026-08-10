# Você recebe um array indexado em 0 de palabras de strings e um caractere x.
# Retorne um array de índices que representam as palavras que contêm o caractere x.

meu_arrayzinho = ["leet","code"]
minha_stringzinha = "e"
meu_arrayzinho_resultado = []

for posicao, palavra in enumerate(meu_arrayzinho):
    if minha_stringzinha in palavra:
        meu_arrayzinho_resultado.append(posicao)


print(meu_arrayzinho_resultado)