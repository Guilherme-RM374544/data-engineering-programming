from pyspark.sql import SparkSession, DataFrame

def read_pedidos(spark: SparkSession, path: str) -> DataFrame:
    """Lê os arquivos CSV da pasta de pedidos com separador ';'."""
    return spark.read \
        .option("header", "true") \
        .option("sep", ";") \
        .option("inferSchema", "true") \
        .csv(path)

def read_pagamentos(spark: SparkSession, path: str) -> DataFrame:
    """Lê os arquivos JSON da pasta de pagamentos."""
    return spark.read \
        .json(path)

def write_parquet(df: DataFrame, output_path: str) -> None:
    """Salva o DataFrame final em formato Parquet."""
    df.write \
        .mode("overwrite") \
        .parquet(output_path)
