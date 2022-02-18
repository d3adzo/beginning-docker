# Compiling a Go binary with Docker 
## My Scenario 
I mostly dev on my macOS laptop. 
I am building a Linux specific binary (utilizes Linux syscalls). Not easily compiled on macOS. I do not want to develop on a Linux VM. 
This method uses Docker to efficiently compile a Go binary, while also statically compiling in necessary libraries (using Gopacket, which uses libpcap).

The docker command being run in the Makefile is
```
docker run --rm=true -itv $(PWD):/mnt alpine:3.7 /mnt/build_static.sh
```
This migrates my files to the docker image and builds it through the `build_static.sh` script. A volume is mounted so I can access the compiled Linux binary.

## Usage
```sh
make # the instructions in the Makefile builds the binary using Docker
ls out/ # compiled Linux binary is in the out/ directory
```