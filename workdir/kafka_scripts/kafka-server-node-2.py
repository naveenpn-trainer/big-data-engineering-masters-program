import os
import subprocess
command = f"kafka-server-start {os.environ.get('KAFKA_HOME')}/etc/kafka/server2.properties"
try:
    subprocess.run(command.split(" "), check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
