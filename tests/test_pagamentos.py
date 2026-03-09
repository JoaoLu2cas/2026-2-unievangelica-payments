import sys
import os

# Adiciona o diretório pai ao sys.path para garantir que o módulo 'app' seja encontrado,
# independente da pasta de onde o aluno rode o pytest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.pagamentos import (
    calcular_desconto,
    aplicar_juros_atraso,
    validar_metodo_pagamento,
    processar_reembolso
)

# ====================================================================
# ÁREA DO ALUNO
# ====================================================================

def test_calcular_desconto():
    # Teste Correto: 10% de desconto sobre 100 deve ser 90
    assert calcular_desconto(100, 10) == 90
    # Teste Correto: 50% de desconto sobre 200 deve ser 100
    assert calcular_desconto(200, 50) == 100

def test_aplicar_juros_atraso():
    # ERRO PROPOSITAL: A expectativa matemática está errada.
    # A função original aplica juros simples de 1% ao dia.
    # Para 100 reais, 5 dias de atraso seriam 105 reais (100 + 100 * 0.01 * 5).
    # O teste abaixo está esperando 150, como se fosse 10% ao dia.
    # ATIVIDADE: Corrigir a expectativa matemática abaixo para o valor correto (1% ao dia).
    assert aplicar_juros_atraso(100, 5) == 150
    assert aplicar_juros_atraso(100, 0) == 100

# TODO: Implementar Testes: Crie os testes para a função validar_metodo_pagamento
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um método de pagamento aceito.
# 2 - Teste um método rejeitado.

# TODO: Implementar Testes: Crie os testes para a função processar_reembolso
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um reembolso válido (valor reembolsado menor ou igual ao pago).
# 2 - Teste um caso de erro, simulando uma regra de negócio que restringe o reembolso (deve retornar -1).
