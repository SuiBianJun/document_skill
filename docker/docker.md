1、docker与vm 虚拟机的比较

![](./pic/docker_vm.png)

![](./pic/docker_vm2.png)

２、docker常用命令

帮助命令：

`docker version`　`docker info`　`docker --help`

镜像命令：

`docker images -a` 　列出本地所有镜像

`docker search xxImage`　搜索镜像

 `docker pull xxImage`　拉取镜像

 `docker rmi xxImage` 删除镜像。如果该镜像曾经在容器中运行过，需要先删除相关容器才可以删除镜像

容器命令：

`docker run [options] xxImage [command]` 新建并启动容器

```shell
docker run -it xxImage  # 交互式运行容器
```

`docker start containerID/containerName` 启动已停止的容器

`docker restart containerID/containerName` 重启已创建的容器

`docker stop containerID/containerName` 停止容器

`docker kill containerID/containerName` 强制停止容器

`docker ps` 列出正在运行的容器信息

`docker rm containerID` 删除容器

`exit` 退出容器，并停止容器

`ctrl + p + q` 退出容器，容器不停止

`docker run -d xxImage` 后台运行容器。如果容器中没有前台应用运行，容器会直接退出，docker ps不会存在该容器

`docker logs containerID`　查看容器日志

`docker top containerID`  查看容器中运行的进程

`docker inspect containerID` 　查看容器运行信息

`docker exec -it containerID　command　`　在正在运行的容器中执行命令，并返回结果。

`docker attach containerID` 重新进入到正在运行容器中

`docker cp containerID:/XX/YY路径　宿主机路径`　拷贝容器中的文件到宿主机