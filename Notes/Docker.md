# Docker

- docker image vs container
  - https://stackify.com/docker-image-vs-container-everything-you-need-to-know/
  - An Image is the application we want to run
  - A Container is an instance of that image running as a process

- docker-airflow github
https://github.com/puckel/docker-airflow

## common commands
```
# check client and server version
# if the versions of local and server are diff, that is fine.
docker version

# find docker commands
docker

# check docker info
docker info
```

## useful commands
```
# pull images
docker pull redis

# run images and create container
docker run redis

# run images and create container in detached model
docker run -d redis

# check running containers
docker container ls
docker ps 

# stop container
docker container stop container_id
docker stop container_id

# remove container
docker container remove container_id

# process list in one container 
docker container top

# debugging
docker log container_id
docker exec -it container_id /bin/bash
docker exec -it name /bin/bash

# remove any resources (images, containers, volumes, and networks)
docker system prune

# To additionally remove any stopped containers and all unused images (not just dangling images)
docker system prune -a
```

