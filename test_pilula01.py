from pilula01 import acao_semaforo, VERDE, AMARELO, VERMELHO

def test_verde():
    assert acao_semaforo(VERDE) == "Siga"

def test_amarelo():
    assert acao_semaforo(AMARELO) == "Atenção"

def test_vermelho():
    assert acao_semaforo(VERMELHO) == "Pare"

def test_cor_invalida():
    assert acao_semaforo("") == "Cor inválida"