#!/usr/bin/env python3

import subprocess
topic = input("Enter topic name? ")
partitions = input("Enter number of partitions? ")
command = f"kafka-topics --create --bootstrap-server localhost:9092 --partitions {partitions} --replication-factor 1 --topic {topic}"
try:
    subprocess.run(command.split(" "), check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

