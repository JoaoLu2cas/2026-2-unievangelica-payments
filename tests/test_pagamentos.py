import pytest
from app.pagamentos import (
    calcular_desconto,
    aplicar_juros_atraso,
    validar_metodo_pagamento,
    processar_reembolso
)

def test_calcular_desconto():
    # Arrange
    valor = 100
    percentual = 10
    
    # Act
    resultado = calcular_desconto(valor, percentual)
    
    # Assert
    assert resultado == 90

def test_aplicar_juros_atraso():
    # Arrange
    valor_pago = 100
    dias_atraso = 5
    dias_ok = 0
    
    # Act
    resultado_com_atraso = aplicar_juros_atraso(valor_pago, dias_atraso)
    resultado_sem_atraso = aplicar_juros_atraso(valor_pago, dias_ok)
    
    # Assert
    # TODO: Corrigir o erro matemático abaixo (Juros simples de 1% ao dia)
    # 100 + (100 * 0.01 * 5) deveria ser 105.0, não 150.0
    assert resultado_com_atraso == 105
    assert resultado_sem_atraso == 100

def test_validar_metodo_pagamento():
    """
    MISSÃO: Implementar testes para validar_metodo_pagamento.
    Use a estrutura AAA (Arrange, Act, Assert).
    Dica: Teste pelo menos um método aceito (ex: 'pix') e um rejeitado (ex: 'cheque').
    """
    # Arrange
    metodo_pagamento_correto = "pix"
    metodo_pagamento_incorreto = "carnê casas Bahia"
    # Act
    resultado_valido = validar_metodo_pagamento(metodo_pagamento_correto) 
    resultado_invalido = validar_metodo_pagamento(metodo_pagamento_incorreto) 
    # Assert
    assert resultado_valido is True, f"Deveria aceitar {metodo_pagamento_correto}"
    assert resultado_invalido is False, f"Não deveria aceitar {metodo_pagamento_incorreto}"

def test_processar_reembolso():
    """
    MISSÃO: Implementar testes para processar_reembolso.
    Use a estrutura AAA (Arrange, Act, Assert).
    Dica: Teste o cenário de reembolso válido e o cenário de erro (-1).
    BÔNUS: Teste o valor limite (reembolso == valor_pago).
    """
    # Arrange
    valor_pago = 100
    valor_reembolso = 50 
    # Act
    resultado = processar_reembolso(valor_pago, valor_reembolso)
    # Assert
    assert resultado == 50 

    # Cenário de erro
    #Arrange
    valor_pago_errado = 100
    valor_pago_errado_reembolso = 150
    #Act
    resultado_erro = processar_reembolso(valor_pago_errado, valor_pago_errado_reembolso)
    #Assert
    assert resultado_erro == -1

    #Cenário bonus
    #Arrange
    valor_total = 100
    #Act
    resultado_limite = processar_reembolso(valor_total, valor_total)
    #Assert
    assert resultado_limite == 0





    pass
