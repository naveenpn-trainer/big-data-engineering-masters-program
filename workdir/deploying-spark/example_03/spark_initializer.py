from pyspark.sql import SparkSession

def get_spark_session():
    return SparkSession.builder.getOrCreate()