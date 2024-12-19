from pyspark.sql import SparkSession
from pyspark.sql.functions import col,count
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()
    user_df = spark.read.csv(path="../../resources/dataset/users/csv_format/users_001.csv",
                             header=True,
                             inferSchema=True)
    user_df.groupBy("designation").agg(count("*").alias("total_count")).sort(col("total_count").desc()).show()
