from pyspark.sql import  SparkSession
from pyspark.sql.functions import col

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Spark Demo App").getOrCreate()
    user_df = spark.read.csv(path="../dataset/users/users.dat",
                             header=True,
                             inferSchema=True,
                             sep="|")
    user_df.show(n=3,truncate=False)
    user_df.printSchema()
    user_df.select(col("id").alias("user_id"),col("designation")).show(n=3)

    for column in user_df.columns:
        print(column)


