from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Spark Demo App").getOrCreate()
