from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Spark Demo App").getOrCreate()
    product_information_df = spark.read.json(path="../dataset/product_Information_001.json", multiLine=True)
    product_information_df.printSchema()
    product_information_df.select(col("details.battery.capacity")).show()

    product_information_df.select(col("name"), col("sellers")[1]).show()

    product_information_df.select(col("name"), size(col("sellers")).alias("No. of sellers")).show()

    print("Write a pyspark code to fetch the product names and their average rating")
    (product_information_df.select("name", explode("reviews.rating").alias("ratings"))
     .groupBy("name").agg(avg("ratings").alias("average_rating"))
     .orderBy("average_rating", ascending=False).show())

    product_information_df.filter(col("details.screen.resolution").like("1920%")).select("name").show()

    product_information_df.filter("details.screen.resolution LIKE '1920%'").select("name").show()