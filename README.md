#### Dockerize a simple python web application.

The docker-compose.yml file  configure the application and its dependencies or services

`
services:
  app:
    build: .
    container_name: python_server
    command: uvicorn src.main:app --host 0.0.0.0 --port 80 --reload
    ports:
      - 80:80
    volumes:
      - .:/code
    depends_on:
      - redis
 
  

  redis:
     image: redis:alpine

 `

Run `docker-compose up --build` to build application. 

Application runs on localhost:80.
