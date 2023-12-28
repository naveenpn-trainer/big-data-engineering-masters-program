#docker pull npnnaveenpn/data_science_and_engineering:v2
docker container kill naveenpn
docker container remove naveenpn
#docker run --name naveenpn -p 50070:50070 -p 8088:8088 -p 9090:9090 -p 8888:8888 -p 4040-4050:4040-4050 -p 7199:7199 -d -it -v "%cd%/workdir":/home/naveenpn/workdir npnnaveenpn/data_science_and_engineering:v1 bash
docker-compose up -d
docker exec -it naveenpn bash