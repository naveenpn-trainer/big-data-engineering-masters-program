from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName(("Spark Demo App")).master("local").getOrCreate()
    print(type(spark))

    spark.read.csv(path="../dataset/users/users.dat", header=True, sep="|", inferSchema=True).write.option("header","true").parquet(path="../dataset/users/par")
