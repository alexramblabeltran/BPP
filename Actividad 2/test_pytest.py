import pytest 
import funciones

def test_coseno():
    assert 1 == funciones.coseno(0)
def test_seno():
    assert 0 == funciones.seno(0)
def test_tangente():
    assert 0 == funciones.tangente(0)
def test_logaritmo_decimal():
    assert 3 == funciones.logaritmo_decimal(1000)
def test_raíz_cuadrada():
    assert 7 == funciones.raíz_cuadrada(49)