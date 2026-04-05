# Exemplo: Contar a frequência de caracteres em uma string

def contar_frequencia(s):
# contar_frequencia: Função que recebe uma string 's' e retorna um dicionário com a contagem de cada caractere.
    frequencia = {}
    # frequencia: Dicionário usado para armazenar a contagem de cada caractere na string.
    for char in s:
    # O loop 'for' itera sobre cada caractere na string. Se o caractere já estiver no dicionário, sua contagem é incrementada.
    # Caso contrário, o caractere é adicionado ao dicionário com uma contagem inicial de 1.
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1
    return frequencia

#Teste da função
string_teste = "abracadabra"
resultado = contar_frequencia(string_teste)
print(resultado)

# Este exemplo demonstra como usar dicionários para contar a frequência de elementos, 
# uma técnica útil em várias aplicações de programação