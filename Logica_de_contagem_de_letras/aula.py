# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte caso é válido:

# Todas as letras desta palavra são maiúsculas, como "EUA".

# Dada uma palavra de string, retorne verdadeiro se o uso de letras maiúsculas está correto.


minha_stringzinha = "EUA"

contador = 0

for letra in minha_stringzinha:
    if letra.isupper():
        contador += 1


print(contador)
print(len(minha_stringzinha))

if contador == len(minha_stringzinha):
    print("Passou no teste!!!!")
else:
    print("REPROVADO")