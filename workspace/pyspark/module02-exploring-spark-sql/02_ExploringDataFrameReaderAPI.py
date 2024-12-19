from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = (SparkSession
             .builder
             .master("local")
             .appName("Spark Demo App")
             .config("spark.jars","../resources/lib/jdbc/mysql-connector-java-8.0.28.jar").getOrCreate())

    # Loading CSV File into DF
    users_csv_df = spark.read.csv(path="../resources/dataset/users/csv_format/users_001.csv",
                                  header=True,
                                  inferSchema=True)

    users_del_df = spark.read.csv(path="../resources/dataset/users/csv_format/users_001.csv",
                                  header=True,
                                  inferSchema=True,
                                  sep="|")

    users_json_df = spark.read.json(path="../resources/dataset/users/json_format/users_002.json",
                                    multiLine=True)


    users_parquet_df = spark.read.parquet("../resources/dataset/users/parquet_format/users.parquet")
    users_parquet_df.show()

    connection_url = "jdbc:mysql://localhost:3306/crime_analysis"
    jdbc_properties = {
        "user":"root",
        "password":"qwerty",
        "driver":"com.mysql.cj.jdbc.Driver"
    }
    users_mysql_df = spark.read.jdbc(url=connection_url,
                                     table="crime",
                                     properties=jdbc_properties)
    users_mysql_df.show()