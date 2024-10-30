set /p topic=Enter topic name?
set /p partitions=Enter number of partitions?
%KAFKA_HOME%\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --partitions %partitions% --replication-factor 1 --topic %topic%