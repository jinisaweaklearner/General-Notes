# Docker

- docker image vs container
https://stackify.com/docker-image-vs-container-everything-you-need-to-know/

- docker-airflow github
https://github.com/puckel/docker-airflow


## useful commands
```
# pull images
docker pull redis

# run images and create container
docker run redis

# run images and create container in detached model
docker run -d redis

# check running containers
docker ps 

# stop container
docker stop container_id

# debugging
docker log container_id
docker exec -it container_id /bin/bash
docker exec -it name /bin/bash

# remove any resources (images, containers, volumes, and networks)
docker system prune

# To additionally remove any stopped containers and all unused images (not just dangling images)
docker system prune -a
```

