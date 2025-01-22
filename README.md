## Steps to run the service
  - [install docker if not availble](#install_docker_if_not_availble)
  - [run the service](#run_the_service)
  - [access the interface and fill the form](#access_the_interface_and_fill_the_form)

### install_docker_if_not_availble

  - for Linux (Ubuntu/Debian)
    ````
    sudo apt update
    sudo apt install docker.io
    ````
  - for windows
    go to ````https://hub.docker.com/```` and download for windows

  - for macOS go for the [guid](https://docs.docker.com/desktop/setup/install/mac-install/#install-and-run-docker-desktop-on-mac)

  - finally,
    use ````docker --version```` to varify the installation

### run_the_service

build the docker image and run the container of the service
````
docker build -t image_build_push_service .
````
````
docker run -v /var/run/docker.sock:/var/run/docker.sock -p 8000:8000 image_build_push_service
````

### access_the_interface_and_fill_the_form
 - open web browser and enter````http://127.0.0.1:8000/````
 - fill the "Docker Hub User Name" and "Docker Hub Password" with the corresponding credentials, credentials wont be saved
 - choose the file and then submit

### docker_images_clean_up
````
docker stop $(docker ps -qa) > /dev/null 2>&1 2>&1 || true
docker rm $(docker ps -qa) > /dev/null 2>&1 2>&1 || true
docker rmi -f $(docker images -qa) > /dev/null 2>&1 2>&1 || true
docker volume rm $(docker volume ls -q) > /dev/null 2>&1 2>&1 || true
docker network rm $(docker network ls -q) > /dev/null 2>&1 2>&1 || true
````
