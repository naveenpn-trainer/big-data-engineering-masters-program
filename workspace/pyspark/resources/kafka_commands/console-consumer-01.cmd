set /p topic=Enter topic name?
%KAFKA_HOME%\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic  %topic%