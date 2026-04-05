# - Aprovado, reprovado ou recuperação:
# Receba a média de um aluno e diga se ele foi aprovado (média >= 7),
# em recuperação (5 >= media < 7) ou
# reprovado (medi < 5).


# 1. Receber a nota do aluno

nota = float(input())

# 2. Fazer a operação e já mostrar o resultado para o aluno.

if nota >= 7.0:
    print("Aluno aprovado")
elif nota >= 5.0 and nota < 7.0:
    print ("Aluno em recuperação")
else:
    print ("Aluno reprovado")