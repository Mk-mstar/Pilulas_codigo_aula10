PRODUTO_ATE1KG = 5.0
PRODUTO_DE1_A_5KG = 10.0
PRODUTO_ACIMA5KG = 18.0
PRODUTO_ZERO = 0.0


def calcular_frete(peso_kg: float) -> float:

    if peso_kg <= 0:
        return PRODUTO_ZERO

    elif peso_kg <= 1:
        return PRODUTO_ATE1KG

    elif peso_kg <= 5:
        return PRODUTO_DE1_A_5KG

    else:
        return PRODUTO_ACIMA5KG