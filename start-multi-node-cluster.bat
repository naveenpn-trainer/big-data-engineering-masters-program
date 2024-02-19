@echo off
setlocal enabledelayedexpansion

:menu
echo Which containers do you want to kill and remove?
echo 1. Login to the existing cluster
echo 2. Create a new cluster and proceed to log in.
echo 3. None
set /p choice=Enter your choice (1-2): 

if "%choice%"=="1" (
    goto compose_up
) else if "%choice%"=="2" (
    set containers=master slave1 slave2 slave3
    goto compose_up	
) else (
    echo Invalid choice. Please try again.
    goto menu
)

for %%c in (%containers%) do (
    docker container kill %%c
    docker container rm %%c
)

:compose_up
docker-compose -f multi-node-cluster/docker-compose.yml up -d 
docker exec -it master bash
