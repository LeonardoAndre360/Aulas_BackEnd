# Dado um array de números inteiros, retorne quantos deles contêm um número par de digitos
# nums = [12,345,2,6,7896] -> Esses valores estão como números inteiros
# novo_array = ["12","345","2","6","7896"] -> Esses valores estarão como string

# 1. Criar um novo Array de strings que vai ter os mesmos valores do primeiro array,porem como strings

novo_array = ["12", "345", "2", "6", "7896"]

# 2. Fazer um looping dentro do novo_Array para fazer a verificação de números com digitos pares
# 3. Fazer a contagem e monstar (printar) na tela o resultado

contator = 0

for i in novo_array:
    if len(i) % 2 == 0:
        contator += 1


print(contator)