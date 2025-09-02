import pytest
import re
from calculadora.calculadora_financeira import calcular_juros_compostos


# ------------------------------------VALIDANDO STRING ------------------------------------------------------
# capital
def test_validar_capital():
    # Definindo a entrada
    capital = "oi"
    taxa = 10
    tempo = 3

    # Executando a função e esperando erro
    mensagem = "O capital investido deve ser um número (int ou float)."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        calcular_juros_compostos(capital, taxa, tempo)
# TAXA
def test_validar_taxa():
    #define entrada
    capital = 1000
    taxa = "oi"
    tempo = 3

    #executando a função e esperando erro
    mensagem = "A taxa de juros deve ser um número (int ou float)."
    with pytest.raises(ValueError,match=re.escape(mensagem)):
        calcular_juros_compostos(capital, taxa, tempo)

# TEMPO
def test_validar_tempo():
    #Definindo a entrada
    capital = 1000
    taxa = 10
    tempo = "oi"

    #executando a função e esperando o erro
    mensagem = "O tempo deve ser um número (int ou float)."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        calcular_juros_compostos(capital, taxa, tempo)

# ------------------------------------VALIDANDO NEGATIVO ----------------------------------------------------
# CAPITAL
def test_validar_capital_negativo():
    # Definindo a entrada
    capital = -1000
    taxa = 10
    tempo = 3

    # Executando a função e esperando erro
    mensagem = "O capital investido não pode ser negativo."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        calcular_juros_compostos(capital, taxa, tempo)

# TAXA
def test_validar_taxa_negativo():
    # Definindo a entrada
    capital = 1000
    taxa = -10
    tempo = 3

    # Executando a função e esperando erro
    mensagem = "A taxa de juros não pode ser negativa."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        calcular_juros_compostos(capital, taxa, tempo)

# TEMPO
def test_validar_tempo_negativo():
    # Definindo a entrada
    capital = 1000
    taxa = 10
    tempo = -3

    # executando a função e esperando o erro
    mensagem = "O tempo não pode ser negativo."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        calcular_juros_compostos(capital, taxa, tempo)


