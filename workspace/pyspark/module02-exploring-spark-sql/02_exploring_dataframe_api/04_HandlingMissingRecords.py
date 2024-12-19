from pyspark.sql import SparkSession
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()
    employee_df = spark.read.csv(path="../../resources/dataset/employee.csv",
                             header=True,
                             inferSchema=True,
                             sep="|")
    employee_df.printSchema()
    # user_df.na.drop().show()
    employee_df.show()
    employee_df.na.fill(-1).na.fill("Anonymous",subset="col_name").na.replace(-1,0,subset="col_id").show()
    # user_df.na.replace(to_replace=None,value=-1).show()
