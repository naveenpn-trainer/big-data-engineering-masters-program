from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    spark = SparkSession.builder.getOrCreate()
    user_df = spark.read.csv(path=input_path, header=True, sep="|", inferSchema=True)

    ## Business Logic

    result_df = user_df.groupby("designation").agg(sum("salary").alias("total_salary"))
    result_df.write.mode("overwrite").csv(path=output_path, sep=",")
