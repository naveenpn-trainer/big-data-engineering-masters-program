from pyspark.sql import SparkSession
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()

    # Sample RDD
    rdd = spark.sparkContext.parallelize([(1, "Alice"), (2, "Bob"), (3, "Charlie")])


    # Create DataFrame from RDD
    df = spark.createDataFrame(rdd,  ["id", "name"])
    df.show()
