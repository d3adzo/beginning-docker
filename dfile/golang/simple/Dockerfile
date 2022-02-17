
# pulling the golang image, version 1.17
FROM golang:1.17 

# create and use /src directory
WORKDIR /src

# copy over main.go file to /src (WORKDIR) as main.go
COPY ./main.go .

# what program will be run when docker container is started. Can take in arguments 
ENTRYPOINT [ "go", "run", "main.go"]

