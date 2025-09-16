# -*- coding: utf-8 -*-
import pytest

def somar(a, b):
    """Soma dois números."""
    return a + b

def test_somar_positivos():
    assert somar(2, 3) == 5
    assert somar(10, 20) == 30

def test_somar_negativos():
    assert somar(-2, -3) == -5
    assert somar(-10, 20) == 10

def test_somar_zero():
    assert somar(5, 0) == 5
    assert somar(0, -5) == -5
    assert somar(0, 0) == 0

def test_somar_float():
    assert somar(2.5, 3.5) == 6.0
    assert somar(-2.5, 3.5) == 1.0

def test_somar_diferentes_tipos():
    with pytest.raises(TypeError):
        somar("2", 3)
    with pytest.raises(TypeError):
        somar(2, "3")
    with pytest.raises(TypeError):
        somar([1,2], 3)