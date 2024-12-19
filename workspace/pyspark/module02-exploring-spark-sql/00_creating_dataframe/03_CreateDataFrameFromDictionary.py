from pyspark.sql import SparkSession
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()
    data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

    df = spark.createDataFrame(data)
    df.show()

