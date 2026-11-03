from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def process_sales_data(df_pedidos: DataFrame, df_pagamentos: DataFrame) -> DataFrame:
    """
    Consolida as informações de pedidos e pagamentos.
    Trata os nomes das colunas e filtra pagamentos recusados.
    """
    # Padroniza os nomes das colunas de pedidos para minúsculo
    for col_name in df_pedidos.columns:
        df_pedidos = df_pedidos.withColumnRenamed(col_name, col_name.lower())

    # Padroniza os nomes das colunas de pagamentos para minúsculo
    for col_name in df_pagamentos.columns:
        df_pagamentos = df_pagamentos.withColumnRenamed(col_name, col_name.lower())

    # Realiza o join passando a string do nome da coluna para evitar duplicidade no Parquet
    df_processado = df_pedidos.join(
        df_pagamentos,
        on="id_pedido",
        how="inner"
    )

    # Filtra pagamentos recusados se a coluna existir
    if "status_pagamento" in df_processado.columns:
        df_processado = df_processado.filter(F.col("status_pagamento") == "recusado")
        
    return df_processado
