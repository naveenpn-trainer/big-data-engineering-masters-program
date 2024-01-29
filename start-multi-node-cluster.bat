docker container kill master
docker container kill slave1
docker container kill slave2
docker container kill slave3
docker container remove master
docker container remove slave1
docker container remove slave2
docker container remove slave3
docker-compose -f multi-node-cluster/docker-compose.yml up -d 
docker exec -it master bash
docker exec -it slave1 bash
docker exec -it slave2 bash