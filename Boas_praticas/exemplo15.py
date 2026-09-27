from collections import Counter
# from collections import Counter: 
# Importa a classe Counter da biblioteca collections, que é usada para contar ocorrências de elementos em um iterável.

def count_occurrences(numbers):
# count_occurrences: Função que recebe uma lista de números e retorna um Counter com a contagem de cada número.
# Utiliza a classe Counter para contar ocorrências de cada número
    return Counter(numbers)
# Counter(numbers): Cria um objeto Counter que conta quantas vezes cada número aparece na lista numbers.

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
occurrences = count_occurrences(numbers)
print(occurrences)
# print(occurrences): Imprime o resultado, mostrando a contagem de cada número na lista.