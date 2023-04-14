### Dockerize a simple python web application.

The docker-compose.yml file  configure the application and its dependencies or services


#### Web App
The application `main.py` is the `src` folder

Either the `Dockerfile` or `docker-compose.yml` YAML file can be used:

1. #### Dockerfile
 
* Run `docker build -t <docker-image-name>` to build the docker image template
* Use `docker run --name <docker-container> -d <docker-image-name>` to build the docker container from the image template

For persisting data in the container use [`volumes`](https://docs.docker.com/storage/volumes/)


2. #### docker-compose.yml

Run `docker-compose up --build` to build application. 

