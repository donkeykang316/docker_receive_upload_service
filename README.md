## Steps to run the service
  - [install docker and python3 if not availble](#install_docker_and_python3_if_not_availble)
  - [run the service](#run_the_service)
  - [access the interface and fill the form](#access_the_interface_and_fill_the_form)

### install_docker_and_python3_if_not_availble

 - install python3
   - for Linux (Ubuntu/Debian)
     ````
     sudo apt update
     sudo apt install python3
     ````
   - for windows
     go to ````python.org/downloads```` and download the latest Python 3 installer

   - for macOS
     ````
     brew install python
     ````

   - finally,
     use ````python3 --version```` to varify the installation

 - install docker
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