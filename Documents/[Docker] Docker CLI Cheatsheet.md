origin: https://docs.docker.com/get-started/docker_cheatsheet.pdf

latest update time: 2023/07/23

## Introduction
Docker provides the ability to package and run an application in a loosely isolated environment called a container. 
The isolation and security allows you to run many containers simultaneously on a given host. Containers are 
lightweight and contain everything needed to run the application, so you do not need to rely on what is currently 
installed on the host. You can easily share containers while you work, and be sure that everyone you share with gets 
the same container that works in the same way.


## Installation

Docker Desktop is available for Mac, Linux and Windows
https://docs.docker.com/desktop

View example projects that use Docker
https://github.com/docker/awesome-compose

Check out our docs for information on using Docker
https://docs.docker.com


## General Commands

#### Start the docker daemon
`docker -d`

#### Get help with Docker. Can also use –help on all subcommands
`docker --help`

#### Display system-wide information
`docker info`


## Images

Docker images are a lightweight, standalone, executable package 
of software that includes everything needed to run an application: 
code, runtime, system tools, system libraries and settings.

### Build an Image from a Dockerfile
`docker build -t <image_name>`

### Build an Image from a Dockerfile without the cache
`docker build -t <image_name> . –no-cache`

### List local images
`docker images`

### Delete an Image
`docker rmi <image_name>`

### Remove all unused images
`docker image prune`


## Docker Hub

Docker Hub is a service provided by Docker for finding and sharing 
container images with your team. Learn more and find images 
at https://hub.docker.com


### Login into Docker
`docker login -u <username>`

### Publish an image to Docker Hub
`docker push <username>/<image_name>`

### Search Hub for an image
`docker search <image_name>`

### Pull an image from a Docker Hub
`docker pull <image_name>`


## Containers

A container is a runtime instance of a docker image. A container 
will always run the same, regardless of the infrastructure. 
Containers isolate software from its environment and ensure 
that it works uniformly despite differences for instance between 
development and staging.

### Create and run a container from an image, with a custom name
`docker run --name <container_name> <image_name>`

### Run a container with and publish a container’s port(s) to the host
`docker run -p <host_port>:<container_port> <image_name>`

### Run a container in the background
`docker run -d <image_name>`

### Start or stop an existing container
`docker start|stop <container_name> (or <container-id>`

### Remove a stopped container
`docker rm <container_name>`

### Open a shell inside a running container
`docker exec -it <container_name> sh`

### Run a container in the background
`docker run -d <image_name>`

### Fetch and follow the logs of a container
`docker logs -f <container_name>`

### To inspect a running container
`docker inspect <container_name> (or <container_id>)`

### To list currently running containers
`docker ps`

### To list currently running containers
`docker ps`

### List all docker containers (running and stopped)
`docker ps --all`

### View resource usage stats
`docker container stats`


## Other Resources

### Full Docker Commands
https://www.runoob.com/docker/docker-command-manual.html

### Dockers Run Options
https://www.runoob.com/docker/docker-run-command.html

OPTIONS说明：

-a stdin: 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；

-d: 后台运行容器，并返回容器ID；

-i: 以交互模式运行容器，通常与 -t 同时使用；

-P: 随机端口映射，容器内部端口随机映射到主机的端口

-p: 指定端口映射，格式为：主机(宿主)端口:容器端口

-t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；

--name="nginx-lb": 为容器指定一个名称；

--dns 8.8.8.8: 指定容器使用的DNS服务器，默认和宿主一致；

--dns-search example.com: 指定容器DNS搜索域名，默认和宿主一致；

-h "mars": 指定容器的hostname；

-e username="ritchie": 设置环境变量；

--env-file=[]: 从指定文件读入环境变量；

--cpuset="0-2" or --cpuset="0,1,2": 绑定容器到指定CPU运行；

-m :设置容器使用内存最大值；

--net="bridge": 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；

--link=[]: 添加链接到另一个容器；

--expose=[]: 开放一个端口或一组端口；

--volume , -v: 绑定一个卷


`docker container run -it --name test alpine sh`

Run a container in interactive way and open a terminal in it, the container name is test and is based on image alpine, and run sh as main app inside container. Remember use `Ctrl+P+Q` to leave container but not close local terminal
