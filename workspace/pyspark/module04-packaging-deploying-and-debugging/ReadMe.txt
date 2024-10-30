Scenario 01
---------------

cd /home/naveenpn/workdir/
$> hdfs dfs -put users.dat /


$> spark-submit --master yarn \
--name "User Analysis" \
user_data_analysis.py /users.dat /output_01

$> hdfs dfs -cat /output_01/part*

Scenario 02
--------------
spark-submit --master yarn \
--name "User Analysis" \
--py-files spark_functions.py,spark_initializer.py  \
user_data_analysis.py /users.dat /output_01



Scenario 03
--------------
spark-submit --master yarn \
--name "User Analysis" \
--py-files example_03.zip  \
user_data_analysis.py /users.dat /output_01


Scenario 04
--------------
spark-submit \
--master yarn \
--name "User Analysis" \
--conf "spark.sql.shuffle.partitions=3" \
--py-files example_03.zip  \
user_data_analysis.py /users.dat /output_01
