#!/bin/sh

docker rm $(docker ps -l -q)
docker rmi $(docker images --format='{{.ID}}' | head -1)