import pytest
from celery_app import calcular_soma, calcular_fatorial

@pytest.fixture(autouse=True)
def mock_sleep(mocker):
    mocker.patch("celery_app.time.sleep", return_value=None)

def test_calcular_soma():
    resultado = calcular_soma(15,25)
    assert resultado == 40

def test_calcular_fatorial_normal():
    resultado = calcular_fatorial(5)
    assert resultado == 120

def test_calcular_fatorial_zero():
    resultado = calcular_fatorial(0)
    assert resultado == 1

def test_calcular_fatorial_negativo():
    with pytest.raises(ValueError, match="O fatorial não está definido para números negativos."):
        calcular_fatorial(-5)