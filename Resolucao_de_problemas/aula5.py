# - Soma 1 a numero_qualquer: Receba um número N e exiba a soma de todos os números de 1 até numero_qualquer

# 1. Receba um número qualquer

numero_qualquer = int(input())

# 2. Entender a lógica da soma



# 3. Exibir a soma de todos os números de 1 até esse número

soma = 0
for i in range(1, numero_qualquer + 1):
    soma += i



print(soma)