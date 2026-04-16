# Exemplo de manipulação de strings e arrays
def count_uppercase_segments(s):
    # Divide a string em segmentos
    segments = s.split()
    # Conta quantos segmentos começam com letras maiúscula
    count = sum(1 for segment in segments if segment[0].isupper())
    return count
# count_uppercase_segments: Esta função divide a string em segmentos usando o split() 
# e conta quantos segmentos começam com uma letra maiúscula usando isupper().

def calculate_running_sum(arr):
    # Calcula a soma acumulada de um array
    running_sum = []
    current_sum = 0
    for num in arr:
        current_sum += num
        running_sum.append(current_sum)
    return running_sum
# calculate_running_sum: Esta função calcula a soma acumulada de um array, 
# adicionando cada elemento ao total acumulado e armazenando o resultado em uma nova lista

# Testando as funções
string_example = "Hello World This is Python"
array_example = [1, 2, 3, 4, 5] 

print("Números de segmentos com maiúsculas:", count_uppercase_segments(string_example))
print("Soma acumulada do array:", calculate_running_sum(array_example))

# O código demonstra como manipular strings e arrays de forma eficaz utilizando funções básicas do Python
# para resolver problemas comuns.