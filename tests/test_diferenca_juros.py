import pytest
import re
from calculadora.calculadora_financeira import calcular_diferenca_juros


def test_validar_entrada():
    capital_inicial = 8.9
    taxa_anual= 9.9
    tempo_anos = 7

    # Execute o código
    resultado = calcular_diferenca_juros(capital_inicial, taxa_anual, tempo_anos)

    # checar a saída
    assert resultado == (2.17)