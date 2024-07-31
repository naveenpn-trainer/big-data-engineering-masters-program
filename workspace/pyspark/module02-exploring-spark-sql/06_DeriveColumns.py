from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, when, col
from data_source_util import DataSource

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("Spark Demo App").getOrCreate()
    user_df = DataSource.create_users_df_from_csv(spark)
    user_df.withColumn("category", lit("Not Defined")).show()

    user_df.withColumn("category", when(col("salary") > 80000, "Upper Class")
                       .when(col("salary")>=50000,"Middle Class")
                       .when(col("salary")>1,"Lower Class")
                       .otherwise("Invalid Salary")).show(n=5)
