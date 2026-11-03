from spark.session_manager import get_spark_session
from data.io_handler import read_pedidos, read_pagamentos, write_parquet
from business.sales_processor import process_sales_data
from config.settings import PATH_PEDIDOS, PATH_PAGAMENTOS, PATH_OUTPUT

def run_pipeline():
    print("Iniciando o Pipeline PySpark...")
    
    # 1. Inicia a sessão Spark
    spark = get_spark_session()
    print("SparkSession criada com sucesso.")
    
    # 2. Leitura dos Datasets
    print(f"Lendo pedidos em: {PATH_PEDIDOS}")
    df_pedidos = read_pedidos(spark, PATH_PEDIDOS)
    
    print(f"Lendo pagamentos em: {PATH_PAGAMENTOS}")
    df_pagamentos = read_pagamentos(spark, PATH_PAGAMENTOS)
    
    # 3. Processamento das Regras de Negócio
    print("Aplicando regras de negócio...")
    df_resultado = process_sales_data(df_pedidos, df_pagamentos)
    
    # 4. Escrita do resultado final em Parquet
    print(f"Salvando resultado Parquet em: {PATH_OUTPUT}")
    write_parquet(df_resultado, PATH_OUTPUT)
    
    print("Pipeline concluído com sucesso!")
    spark.stop()
