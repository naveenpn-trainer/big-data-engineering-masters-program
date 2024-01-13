import subprocess
topic = input("Enter topic name? ")
command = f"kafka-console-producer --broker-list localhost:9092 --topic {topic}"
try:
    subprocess.run(command.split(" "), check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
