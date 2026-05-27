from main import calcular_desconto
import pytest

def test_desconto_valido():

    valor=100

    resultado=calcular_desconto(valor,"GEEK20")

    assert resultado==80


def test_sem_desconto():

    valor=100

    resultado=calcular_desconto(valor,"ABC")

    assert resultado==100