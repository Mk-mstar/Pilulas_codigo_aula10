
from pilula05 import aplicar_cupom


def test_cupom10():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10
    assert aplicar_cupom("cupom10", 200.0) == 0.10


def test_cupom25_valido():
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25


def test_cupom25_invalido():
    assert aplicar_cupom("CUPOM25", 50.0) == 0.0


def test_descontovip_valido():
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35


def test_descontovip_invalido():
    assert aplicar_cupom("DESCONTOVIP", 300.0) == 0.0


def test_cupom_invalido():
    assert aplicar_cupom("CUPOM_FALSO", 500.0) == 0.0