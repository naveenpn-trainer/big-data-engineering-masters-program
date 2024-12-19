from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == '__main__':
    spark = (SparkSession
             .builder
             .master("local")
             .appName("Spark Demo App")
             .getOrCreate())

    # Loading CSV File into DF
    users_csv_df = spark.read.csv(path="../resources/dataset/users/csv_format/users_001.csv",
                                  header=True,
                                  inferSchema=True)

    # users_csv_df.show()
    users_csv_df.select("id","age").show()

    users_csv_df.select(col("id"),
                        col("age").alias("user_age")).show()

    users_csv_df.filter(col("designation") == "Technician").show()

    users_csv_df.filter(col("designation").isin("Technician","Other")).show()