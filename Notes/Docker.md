# Docker

## general commands
```
# check client and server version
# if the versions of local and server are diff, that is fine.
docker version

# find docker commands
docker

# check docker info
docker info

# display info for images and volumes
docker image inspect mysql
docker volume inspect 2f30806593048ceccb256592c8b9e75b7fbef814dd41b76878ceb7eb6aa14c5d
```

## pull
```
docker pull redis

# pull image with a tag
docker pull redis:tags
```

## run stop remove
```
# run images and create container
docker run redis

# run images and create container in background
docker run -d redis

# run a container and name volume
docker container run -d --name mysql3 -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql

# stop container
docker container stop container_id
docker stop container_id

# remove container
docker container rm container_id

# force to remove running containers
docker container rm -f container_id

# remove any resources (images, containers, volumes, and networks)
docker system prune

# To additionally remove any stopped containers and all unused images (not just dangling images)
docker system prune -a
```

## list 
```
# show just running containers
docker container ls 

# show all containers
docker container ls -a

# show all volumes
docker volume ls

# show all images
docker image ls
```

## check and debug
```
# get inside docker
docker container run -it --name ubuntu ubuntu

# check the logs of containers
docker logs container_id

# check the info of volume
docker volume inspect mysql-db

# check the info of container
docker container inspect mysql3

# get inside of container | Run a command in a running container
docker container exec -it nginx bash

```

### image vs container
  - https://stackify.com/docker-image-vs-container-everything-you-need-to-know/
  - An Image is the application we want to run
  - A Container is an instance of that image running as a process

### Volumes
- Containers are usually immutable and ephemeral 
- volume is "persistent data"; need to be deleted `manually`

### Bind mounts vs Volumes
Bind mounts: A bind mount is a file or folder stored anywhere on the container host filesystem, mounted into a running container. The main difference a bind mount has from a volume is that since it can exist anywhere on the host filesystem, processes outside of Docker can also modify it.

Volumes: Volumes are the preferred way to store persistent data Docker containers create or use. The host filesystem also stores volumes, similar to bind mounts. However, Docker completely manages them and stores them under C:\ProgramData\docker\volumes by default.

### resources
- docker-airflow github
https://github.com/puckel/docker-airflow