#!/bin/sh
# many thanks to @negbie
# https://github.com/google/gopacket/issues/424#issuecomment-369551841

# install libraries
set -ex
apk update
apk add linux-headers musl-dev gcc go libpcap-dev ca-certificates git

# go specific 
mkdir /go
export GOPATH=/go
mkdir -p /go/src/github.com/d3adzo
mkdir -p /mnt/out
cp -a /mnt /go/src/github.com/d3adzo/poetry
cd /go/src/github.com/d3adzo/poetry
go get -v all

# build the go binary
go build --ldflags '-linkmode external -extldflags "-static -s -w"' -v ./

# copy the built binary to the mounted directory
cp ./poetry /mnt/out/
