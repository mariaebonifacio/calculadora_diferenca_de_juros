"""
Testes para a função calcular_juros_simples.

Este arquivo de teste está organizado em três categorias lógicas:
- happy_path: Testa os cenários de sucesso com entradas válidas e típicas.
- edge_cases: Testa os casos limites e especiais (ex: valores zero).
- error_handling: Testa se a função levanta as exceções corretas para entradas inválidas.
"""

import pytest
from calculadora.calculadora_financeira import calcular_juros_simples



# --- Categoria 1: Testes de Caminho Feliz (Happy Path) ---

@pytest.mark.happy_path
@pytest.mark.parametrize(
    "principal, taxa, tempo, montante_esperado",
    [
        # Caso 1: Valores inteiros padrão
        (1000.00, 5.0, 2.0, 1100.00),
        
        # Caso 2: Período de tempo mais longo
        (5000.00, 3.5, 10.0, 6750.00),
        
        # Caso 3: Valores com casas decimais
        (2550.75, 4.2, 1.5, 2711.45),
        
        # Caso 4: Taxa de juros alta
        (100.00, 100.0, 1.0, 200.00),
    ],
    ids=["inteiros_padrao", "longo_periodo", "valores_decimais", "taxa_alta"]
)
def test_calculo_juros_simples_cenarios_validos(principal, taxa, tempo, montante_esperado):
    """Verifica se a função calcula corretamente o montante para diversos cenários válidos."""
    # AAA Pattern: Arrange (Organizar), Act (Agir), Assert (Verificar)
    # Arrange: Os parâmetros já são o nosso arranjo.
    
    # Act: Executamos a função a ser testada.
    resultado = calcular_juros_simples(principal, taxa, tempo)
    
    # Assert: Verificamos se o resultado é o esperado.
    # Usamos pytest.approx para evitar problemas de precisão com floats.
    assert resultado == pytest.approx(montante_esperado)




# --- Categoria 2: Testes de Casos Limites (Edge Cases) ---

@pytest.mark.edge_cases
@pytest.mark.parametrize(
    "principal, taxa, tempo, montante_esperado",
    [
        # Caso 1: Taxa de juros zero não deve render juros.
        (1000.00, 0.0, 5.0, 1000.00),

        # Caso 2: Tempo zero não deve render juros.
        (1000.00, 5.0, 0.0, 1000.00),
        
        # Caso 3: Principal zero deve resultar em zero.
        (0.00, 10.0, 10.0, 0.00),
    ],
    ids=["taxa_zero", "tempo_zero", "principal_zero"]
)
def test_calculo_juros_simples_casos_limites(principal, taxa, tempo, montante_esperado):
    """Verifica o comportamento da função com entradas de valor zero."""
    resultado = calcular_juros_simples(principal, taxa, tempo)
    assert resultado == pytest.approx(montante_esperado)




# --- Categoria 3: Testes de Tratamento de Erros (Error Handling) ---

@pytest.mark.error_handling
@pytest.mark.parametrize(
    "principal, taxa, tempo",
    [
        (-1000.00, 5.0, 2.0),  # Principal negativo
        (1000.00, -5.0, 2.0),   # Taxa negativa
        (1000.00, 5.0, -2.0),   # Tempo negativo
    ],
    ids=["principal_negativo", "taxa_negativa", "tempo_negativo"]
)
def test_juros_simples_levanta_erro_para_valores_negativos(principal, taxa, tempo):
    """
    Verifica se a função levanta um ValueError para qualquer entrada negativa,
    e se a mensagem de erro está correta.
    """
    # Usamos o 'match' para garantir que a mensagem de erro contém o texto esperado.
    with pytest.raises(ValueError, match="devem ser valores não-negativos"):
        calcular_juros_simples(principal, taxa, tempo)



@pytest.mark.error_handling
@pytest.mark.parametrize(
    "principal, taxa, tempo",
    [
        # Caso 1: Enviando um texto como capital
        ("mil", 5.0, 2.0),
        # Caso 2: Enviando uma lista como taxa
        (1000, [5.0], 2.0),
        # Caso 3: Enviando uma lista de string como tempo
        (1000, 5.0, ["dois anos"]),
    ],
    ids=["capital_como_texto","juros_como_lista","tempo_como_lista_de_string"]
)

def test_juros_simples_levanta_erro_para_tipos_invalidos(principal, taxa, tempo):
    """Verifica se a função levanta um TypeError ao receber tipos não-numéricos."""
    # O Python levantará um TypeError naturalmente ao tentar fazer contas com strings.
    # O teste garante que esse comportamento de falha esperado aconteça.
    with pytest.raises(TypeError, match="Os valores devem ser numéricos"):
        calcular_juros_simples(principal, taxa, tempo)