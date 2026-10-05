def add(a, b):
# add: Função simples que retorna a soma de dois números
    return a + b
def test_add():
# test_add: Função de teste que verifica se a função add está retornando os resultados esperados para diferentes entradas.
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
# assert: Verifica se a expressão é verdadeira; se não for, o teste falha, indicando que a função add não está funcionando conforme o esperado.