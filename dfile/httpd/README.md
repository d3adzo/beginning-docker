# Apache2 Dockerfile

## Usage
```sh
docker build -t httpd . # build the apache2 docker image with the Dockerfile
docker run -d -p 8080:80 httpd # Run the docker container in the background, reachable on host port 8080
curl localhost:8080 # query the webserver
docker exec -it <container_id> /bin/bash # get a shell on the running docker container and modify the file
curl localhost:8080 # query the modified webserver
```