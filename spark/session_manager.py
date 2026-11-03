from pyspark.sql import SparkSession

def get_spark_session(app_name: str = "Projeto-PySpark-Dupla2") -> SparkSession:
    """Cria e retorna uma sessão Spark configurada para execução local."""
    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .getOrCreate()
