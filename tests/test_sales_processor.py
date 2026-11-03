import pytest
from pyspark.sql import SparkSession
from business.sales_processor import process_sales_data

@pytest.fixture(scope="session")
def spark():
    """Cria uma SparkSession temporária para execução dos testes."""
    return SparkSession.builder \
        .master("local[1]") \
        .appName("Test-PySpark") \
        .getOrCreate()

def test_process_sales_data(spark):
    # Dados fictícios com a estrutura das colunas reais
    dados_pedidos = [
        ("101", "Notebook", 3500.0, 1, "2025-01-01", "SP", "C001"),
        ("102", "Mouse", 150.0, 2, "2025-01-02", "RJ", "C002")
    ]
    df_pedidos = spark.createDataFrame(
        dados_pedidos, 
        ["ID_PEDIDO", "PRODUTO", "VALOR_UNITARIO", "QUANTIDADE", "DATA_CRIACAO", "UF", "ID_CLIENTE"]
    )

    dados_pagamentos = [
        ("101", "cartao_credito", "aprovado"),
        ("102", "boleto", "recusado")
    ]
    df_pagamentos = spark.createDataFrame(
        dados_pagamentos, 
        ["id_pedido", "forma_pagamento", "status_pagamento"]
    )

    df_resultado = process_sales_data(df_pedidos, df_pagamentos)

    # Deve manter apenas o pedido 102 que teve pagamento recusado
    assert df_resultado.count() == 1
    ids_resultantes = [row.id_pedido for row in df_resultado.collect()]
    assert "102" in ids_resultantes
