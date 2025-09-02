"""
Módulo para cálculos financeiros básicos.
"""

def calcular_juros_simples(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula o montante final de um investimento com base na fórmula de juros simples.

    Esta função aplica a taxa de juros sobre o capital inicial durante o
    período especificado e retorna a soma do capital com os juros acumulados.

    A fórmula utilizada é: M = C * (1 + (i * t)), onde:
      - M = Montante final
      - C = Capital inicial
      - i = Taxa de juros (em formato decimal)
      - t = Tempo

    Args:
        capital_inicial (float): O valor do capital inicial a ser investido.
            Ex: 1000.00
        taxa_anual (float): A taxa de juros anual em formato percentual.
            Ex: 5 para 5%
        tempo_anos (float): O período do investimento, em anos. Pode ser fracionado.
            Ex: 2.5 para dois anos e meio.

    Returns:
        float: O montante final (capital + juros), arredondado para 2 casas decimais.

    Raises:
        ValueError: Se qualquer um dos argumentos (capital, taxa, tempo)
            for um valor negativo.

    Example:
        >>> calcular_juros_simples(1000.00, 5.0, 2.0)
        1100.00
        >>> calcular_juros_simples(2500.00, 3.5, 10.0)
        3375.00
    """
    
    # --------IFs de Validação

    # capital inicial
    if not isinstance(capital_inicial, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    # taxa anual
    if not isinstance(taxa_anual, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    # tempo anos
    if not isinstance(tempo_anos, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    # Validando valores negativos
    if capital_inicial < 0 or taxa_anual < 0 or tempo_anos < 0:
        raise ValueError("devem ser valores não-negativos")
    
    # ------CÁLCULO 

    # Converter taxa percentual para decimal
    taxa_decimal = taxa_anual / 100
    # Fórmula dos juros simples
    montante = capital_inicial * (1 + taxa_decimal * tempo_anos)

    # round serve para arredondar os numeros
    return round(montante, 2)



def calcular_juros_compostos(capital_investido:float, taxa_juros:float, tempo:int) -> tuple:

    # ---------IFs DE VALIDAÇÃO

    # Validação do capital investido
    if not isinstance(capital_investido, (int, float)):
        raise ValueError("O capital investido deve ser um número (int ou float).")
    if capital_investido < 0:
        raise ValueError("O capital investido não pode ser negativo.")
    # Validação da taxa de juros
    if not isinstance(taxa_juros, (int, float)):
        raise ValueError("A taxa de juros deve ser um número (int ou float).")
    if taxa_juros < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")
    # Validação do tempo
    if not isinstance(tempo, (int, float)):
        raise ValueError("O tempo deve ser um número (int ou float).")
    if tempo < 0:
        raise ValueError("O tempo não pode ser negativo.")

    # ------- Cálculo dos juros compostos

    montante = capital_investido * (1 + taxa_juros / 100) ** tempo
    juros = montante - capital_investido

    # RETURN
    return juros, montante



def calcular_diferenca_juros(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula a diferença de juros entre o calculo do montante do juros composto e o montante do juros simples a partir de um capital inicial, uma taxa de juros e um período de tempo.

    A fórmula usada para calcular os juros compostos é:
        diferenca_juros = MC - MS
    Onde:
        MC = Montante final do calculo de juros composto
        MS = Montante final do calculo de juros simples

    Parâmetros:
    -----------
    capital_investido : float
        O valor do capital inicial (P). Deve ser um número não negativo.
    
    taxa_juros : float
        A taxa de juros anual (r), expressa em porcentagem (ex: 5 para 5%). Deve ser um número não negativo.

    tempo : float
        O tempo de investimento (t), em anos ou períodos definidos. Deve ser um número não negativo.

    Retorno:
    --------
        float: A diferença entre o montate resultante do calculo do juros composto e o montante do calculo do juros simples, arredondado para 2 casas decimais.
    """

    # --------- IFs de Validação

    # capital inicial
    if not isinstance(capital_inicial, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    # taxa anual
    if not isinstance(taxa_anual, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    # tempo em anos
    if not isinstance(tempo_anos, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    # validação dos valores negativos
    if capital_inicial < 0 or taxa_anual < 0 or tempo_anos < 0:
        raise ValueError("devem ser valores não-negativos")

    # ------- CÁLCULO

    montante_s = calcular_juros_simples(capital_inicial, taxa_anual, tempo_anos)
    montante_c = calcular_juros_compostos(capital_inicial, taxa_anual, tempo_anos) [1]
    diferenca = montante_c - montante_s
    
    # Retornar a diferença arredondada para 2 casas decimais
    return round(diferenca, 2)
