Scenario 01
---------------
$> spark-submit --master yarn \
--name "User Analysis" \
user_data_analysis.py /u.user /output_17

$> hdfs dfs -cat /output_17/part*

Scenario 02
--------------
spark-submit --master yarn \
--name user_analysis \
--py-files spark_functions.py,spark_initializer.py  \
user_data_analysis.py /u.user /output_12_05
Scenario 03
--------------
spark-submit --master yarn \
--name user_analysis \
--py-files supporting_files.zip  \
user_data_analysis.py /u.user /output_12_05
Scenario 04
--------------
spark-submit \
--master yarn \
--name user_analysis \
--conf "spark.sql.shuffle.partitions=3" \
--py-files supporting_files.zip  \
user_data_analysis.py /u.user /output_12_05
