# -*- coding: utf-8 -*-
import pytest

def dividir(a, b):
    """Divide dois números. Lança erro se o divisor for zero."""
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

def test_dividir_sucesso():
    assert dividir(10, 2) == 5.0
    assert dividir(15, 3) == 5.0
    assert dividir(100, 4) == 25.0
    assert dividir(-10, 2) == -5.0
    assert dividir(10, -2) == -5.0
    assert dividir(0, 5) == 0.0


def test_dividir_zero_divisor():
    with pytest.raises(ValueError) as excinfo:
        dividir(10, 0)
    assert "O divisor não pode ser zero." in str(excinfo.value)

def test_dividir_zero_numerador():
    assert dividir(0, 5) == 0.0

def test_dividir_numeros_grandes():
    assert dividir(1000000, 1000) == 1000.0

def test_dividir_numeros_decimais():
    assert dividir(10.5, 2.5) == 4.2
    assert dividir(10.0, 2.0) == 5.0

def test_dividir_negativos():
    assert dividir(-10,-2) == 5.0