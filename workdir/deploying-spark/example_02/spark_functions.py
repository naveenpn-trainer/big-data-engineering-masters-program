from pyspark.sql.functions import *
def group_by(df,column_name, fn_name,agg_name):
    if fn_name =="sum":
        return df.groupby(column_name).agg(sum(agg_name).alias("total_salary"))
    elif fn_name == "avg":
        return df.groupby(column_name).agg(avg(agg_name).alias("total_salary"))