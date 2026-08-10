# A tradução da língua Berland para a língua Birland não é uma tarefa fácil.
# Essas línguas são muito semelhantes:
# Uma palavra berlandesa difere um pouco de uma palavra birlandesa com o mesmo significado:
# é escrita (e pronunciada) inversamente.
# Por exemplo, palavra berlandês "code" corresponde a uma palavra birlandesa "edoc".
# Porém, cometer um erro durante durante a "tradução" é fácil.
# Vasya tradiziu a palavra s de Berlandish para Birlandish com t.
# Ajude-o: descubra se ele traduziu a palavra corretamente.

primeira_stringzinha = "code"
segunda_stringzinha = "edoc"

if primeira_stringzinha == segunda_stringzinha[::-1]:
    print("Passou no teste!!!")
else:
    print("reprovado")