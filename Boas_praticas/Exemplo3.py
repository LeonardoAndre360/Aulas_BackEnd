# Gerar uma lista de quadrados de números ímpares de 1 a 10

square_of_odds = [x**2 for x in range(1, 11) if x % 2 != 0]
print(square_of_odds)

# range(1, 11): Gera números de 1 a 10.
# x % 2 != 0 : Filtra apenas os números ímpares.
# x**2 : Calcula o quadrado de cada número ímpar.
# O resultado é uma lista de quadrados de números ímpares de 1 a 10, 
# demonstrando a eficiência e clareza do List Comprehension