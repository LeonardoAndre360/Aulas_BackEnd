

try:
    numero = int(input("Digite um número:\n"))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("ERRO: entrada inválida. Por favor, digite um número:\n")
except ZeroDivisionError:
    print("ERRO: Não é possivel dividir por Zero.")
