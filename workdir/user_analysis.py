import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def main(arg):
    data_path = arg[1]
    spark = SparkSession.builder.getOrCreate()
    user_df = spark.read.csv(path=data_path,
                             header=True,
                             sep="|",
                             inferSchema=True)
    user_df.groupby(col("col_state")).count().show()


if __name__ == '__main__':
    main(sys.argv)
