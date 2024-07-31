from pyspark.sql import SparkSession

def get_spark_session():
    return SparkSession.builder.appName("DUMMY NAME").config("spark.sql.shuffle.partitions","4").getOrCreate()