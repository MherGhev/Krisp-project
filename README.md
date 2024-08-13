# Krisp-project

## Simple recommendation system using microservices

### Overview
This project demonstrates a simple microservice architecture using Flask, Redis, and Docker. The architecture consists of two primary services: the Generator Service and the Invoker Service. These services communicate with each other to generate recommendations based on a random number generator, with local and Redis caching.

### Microservices

#### Generator Service

This service has only one endpoint which creates a random number from 1 to 100. Returns a json like
``` 
{
    "reason": Modelname,
    "result": RandomNumber
}
```

#### Invoker Service

This service has an endpoint ```/recommend``` which returns a cached result if there is one, and if there isn't, does 5 parallel calls to the Generator service and returns the merged result.

### Used Technologies

- Flask - A WSGI web application framework for Python used to build the microservices.
- Redis - An in-memory data structure store used as a cache for the Invoker service.
- Docker - Containerization platform to package the services.

### Getting Started


- Clone the repository
```sh
$ git clone git@github.com:MherGhev/Krisp-project.git
$ cd ./part1
```

- Build and start the application
```sh
$ docker compose build
$ docker compose up
```

- Access the services
The generator service will be available at `http://localhost:8080`
The invoker service will be available at `http://localhost:8081`

- Sending the requests
Send a post request to the generator service like this
`curl -X POST http://localhost:8081/recommend -H "Content-Type: application/json" -d '{"viewerid": "12345"}'
`

### Notes
This README is linked to the whole krisp assignment. You can find part1 (the recommendation system), part2 (the problemset) and code review under the main directory.
