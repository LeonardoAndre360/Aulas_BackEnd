# test_caculator.py

def test_add():
# Test_add: Função de teste que verifica se a função add retorna o resultado correto ao somar dois números
    assert add(2, 3) == 5

def add(a, b):
# add: Função que implementa a soma de dois números inicialmente, 
# o teste test_add é escrito antes da implementação da função add,
# seguindo o ciclo Red_Green_Refactor
    return a + b

if __name__ == "__main__":
    test_add()
    print("Todos os testes passaram.")
# O código é executado chamando test_add, e se o teste passar, 
# uma mensagem é impressa indicando que todos os testes passaram