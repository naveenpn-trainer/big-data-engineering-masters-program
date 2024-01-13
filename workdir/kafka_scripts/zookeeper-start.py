import os
import subprocess
command = f"zookeeper-server-start {os.environ.get('KAFKA_HOME')}/etc/kafka/zookeeper.properties"
try:
    subprocess.run(command.split(" "), check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")


