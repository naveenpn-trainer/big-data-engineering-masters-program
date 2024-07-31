from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
import spark_initializer
import spark_functions

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    spark = spark_initializer.get_spark_session()
    user_df = spark.read.csv(path=input_path, header=True, sep="|", inferSchema=True)

    ## Business Logic
    result_df = spark_functions.group_by(user_df,"designation","sum","salary")
    result_df.write.mode("overwrite").csv(path=output_path, sep=",")
