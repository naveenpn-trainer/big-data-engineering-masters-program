@ECHO OFF
@RD /S /Q %KAFKA_HOME%\frameworks\kafka\kafka-logs"
@RD /S /Q %KAFKA_HOME%\frameworks\kafka\logs"
@RD /S /Q %KAFKA_HOME%\frameworks\kafka\zookeeper-logs"
PAUSE
