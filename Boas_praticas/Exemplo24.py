import pytest

@pytest.fixture
def sample_data():
# @pytest.fixture: Define uma fixture chamada sample_data que prepara dados de exemplo para os testes.
    # Fixture que prepara dados de exemplo
    return {"key1": "value1", "key2": "value2"}

def test_example(sample_data):
    # Teste que utiliza a fixture sample_data
    assert sample_data["key1"] == "value1"
    assert sample_data["key2"] == "value2"
# test_example: Teste que utiliza a fixture sample_data. Ele verifica se os dados preparados pela fixture estão corretos.