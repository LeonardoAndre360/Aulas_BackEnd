# Anton gosta de jogar xadrez, assim como seu amigo Danik.
# Depois de terem jogado n jogos consecutivos.
# Para cada jogo sabe-se quem foi o vencedor - Anton ou Danik.
# Nenhum dos jogos terminou empatado.
# Agora Anton se pergunta: quem ganhou mais jogos, ele ou Danik? Ajude-o a determinar isso.

quantidade_de_jogos = 6
vencedores_de_cada_jogo = "ADAAAA"

quantidade_vitorias_anton = vencedores_de_cada_jogo.count('A')
quantidade_vitorias_danik = vencedores_de_cada_jogo.count('D')

print(f"Quantidade de vitórias do Anton: {quantidade_vitorias_anton}")
print(f"Quantidade de vitórias do Danik: {quantidade_vitorias_danik}")