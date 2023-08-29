#!/bin/bash

docker info 
sleep 1
docker images
sleep 1 
docker ps -a
sleep 1
docker kill $(docker ps -q)
docker rmi $(docker image -q)

