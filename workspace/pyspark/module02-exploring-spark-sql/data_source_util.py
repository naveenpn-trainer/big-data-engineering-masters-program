class DataSource:

    @staticmethod
    def create_users_df_from_csv(spark):
        return spark.read.csv(path="../dataset/users/users.dat",
                             header=True,
                             inferSchema=True,
                             sep="|")


    @staticmethod
    def create_users_df_from_parquet(spark):
        return spark.read.csv(path="../dataset/users/users.parquet",
                             header=True,
                             inferSchema=True,
                             sep="|")