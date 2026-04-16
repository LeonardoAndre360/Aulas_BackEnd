# Retorne a media de todos os salários, com exceção do maior e menor

salario = [4000,3000,1000,2000,5000,6000,500,4500,4700]

novo_array = sorted(salario)

novo_array.remove(novo_array[0])
novo_array.remove(novo_array[-1])

media_dos_salarios = 0

for salario in novo_array:
    media_dos_salarios += salario


print(media_dos_salarios // len(novo_array))