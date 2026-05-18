from pilula02 import (
    calcular_frete,
    PRODUTO_ATE1KG,
    PRODUTO_DE1_A_5KG,
    PRODUTO_ACIMA5KG,
    PRODUTO_ZERO
)


def test_frete_ate_1kg():
    assert calcular_frete(1.0) == PRODUTO_ATE1KG


def test_frete_entre_1_e_5kg():
    assert calcular_frete(1.01) == PRODUTO_DE1_A_5KG
    assert calcular_frete(5.0) == PRODUTO_DE1_A_5KG


def test_frete_acima_5kg():
    assert calcular_frete(5.01) == PRODUTO_ACIMA5KG


def test_frete_zero():
    assert calcular_frete(0) == PRODUTO_ZERO


def test_frete_negativo():
    assert calcular_frete(-10) == PRODUTO_ZERO