from pyspark.sql import SparkSession
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()
    data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
    columns = ["id", "name"]

    df = spark.createDataFrame(data, schema=columns)
    df.show()
