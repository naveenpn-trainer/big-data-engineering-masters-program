from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Spark Demo App").getOrCreate()
    user_df = spark.read.csv(path="../dataset/users/users.dat",
                             header=True,
                             inferSchema=True,
                             sep="|")

    user_df.filter(col("designation") == "technician").show()

    user_df.filter(col("designation").isin("writer", "technician" )).show()

    user_df.filter(col("designation")=="technician").filter(col("gender")=="M").show()

    user_df.filter((col("age")> 50) | (col("salary")>800000)).show()

    print("Filter Records whose designation is 'Technician")
    print(user_df.filter(lower(col("designation"))=="technician").count())