
from pilula04 import calcular_bonus

def test_bonus_excelente():
    assert calcular_bonus(1000, "Excelente") == 200.0
    assert calcular_bonus(2500, "Excelente") == 500.0

def test_bonus_bom():
    assert calcular_bonus(1000, "Bom") == 100.0
    assert calcular_bonus(3000, "Bom") == 300.0

def test_bonus_regular():
    assert calcular_bonus(1000, "Regular") == 20.0
    assert calcular_bonus(5000, "Regular") == 100.0

def test_bonus_ruim():
    assert calcular_bonus(1000, "Ruim") == 0.0

def test_avaliacao_invalida():
    assert calcular_bonus(1000, "Mais ou Menos") == 0.0

def test_salario_negativo():
    assert calcular_bonus(-1000, "Excelente") == 0.0
    assert calcular_bonus(-500, "Bom") == 0.0