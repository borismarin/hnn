# Installing HNN on Mac OS

This guide describes two methods for installing HNN and its prerequisistes on Mac OS (tested on High Sierra):

Method 1: A Docker container running a Linux install of HNN (recommended)
   - The Docker installation fully isolates HNN's python environment and the NEURON installation from the rest of your system, reducing the possibility of version incompatibilities. Additionally, the same Docker container is used for all platforms (Windows/Linux/Mac) meaning it has likely been tested more recently.
   
Method 2: Installing HNN natively on Mac OS (advanced users)
   - This method will run HNN without using virtualization, meaning the GUI may feel more responsive and simulations may run slightly faster. However, the procedure is a set of steps that the user must follow, and there is a possibility that differences in the base environment may require additional troubleshooting. Thus, Method 2 is best suited for advanced users.

## Method 1: Docker install

[Docker Desktop](https://www.docker.com/products/docker-desktop) requires Mac OS Sierra 10.12 or above. For earlier versions of Mac OS, use the legacy version of [Docker Toolbox](https://docs.docker.com/toolbox/overview/).

The only other prerequisite besides docker is an X server. [XQuartz](https://www.xquartz.org/) is free and the recommended option for Mac OS.

### Prerequisite: install XQuartz
1. Download the installer image (version 2.7.11 tested): https://www.xquartz.org/
2. Run the XQuartz.pkg installer within the image, granting privileges when requested.
3. Start the XQuartz application. An "X" icon will appear in the taskbar along with a terminal, signaling that XQuartz is waiting for connections. You can minimize the terminal, but do not close it.
4. Open the XQuartz preferences and navigate to the "security" tab. Make sure "Authenticate connections" is unchecked and "Allow connections from network clients" is checked.
![XQuartz preferences](install_pngs/xquartz_preferences.png)

### Prerequisite (Mac OS Sierra 10.12 or above): install Docker Desktop
1. Download the installer image (requires a free Docker Hub account):
https://hub.docker.com/editions/community/docker-ce-desktop-mac
2. Run the Docker Desktop installer, moving docker to the applications folder.
3. Start the Docker application, acknowledging that it was downloaded from the Internet and you still want to open it.
4. The Docker Desktop icon will appear in the taskbar with the message "Docker Desktop is starting", Followed by "Docker Desktop is running".

### Prerequisite (Mac OS pre-10.12): install Docker Toolbox
1. Download the installer image:
https://docs.docker.com/toolbox/toolbox_install_mac/
2. Run the installer, selecting any directory for installation.
3. Choose "Docker Quickstart Terminal" tool
4. Verify that Docker has started by running the following in the provided terminal window. 
    ```
    docker info
    docker-compose --version
    ```
5. Run the following commands in the same terminal window or by relaunching "Docker Quickstart Terminal".
6. For Docker Toolbox only, we will need to set an IP address in the file docker-compose.yml before starting the HNN container.
    - Get the IP address of the local interface that Docker Toolbox created. It will be named similar to vboxnet1 with an IP address such as 192.168.99.1
      ```
      ifconfig vboxnet1
      ```
    - Edit the docker-compose.yml file in `hnn/installer/mac/`, replacing `host.docker.internal:0` with the IP address such as `192.168.99.1:0` (**The ":0" is required**). Save the file before running the commands below.


### Start HNN
1. Verify that XQuartz and Docker are running. These will not start automatically after a reboot. Check that Docker is running properly by typing the following in a new terminal window.
    ```
    docker info
    ```
2. Clone or download the [HNN repo](https://github.com/jonescompneurolab/hnn). If you already have a previous version of the repository, bring it up to date with the command `git pull origin master` instead of the `git clone` command below.
    ```
    git clone https://github.com/jonescompneurolab/hnn.git
    cd hnn/installer/mac
    ```
3. Start the Docker container. Note: the jonescompneurolab/hnn docker image will be downloaded from Docker Hub (about 1.5 GB). Docker-compose starts a docker container based on the specification file docker-compose.yml and "up" starts the containers in that file and "-d" starts the docker containers in the background.
    ```
    docker-compose up -d
    ```    
4. The HNN GUI should show up and you should now be able to run the tutorials at: https://hnn.brown.edu/index.php/tutorials/
   * A directory called "hnn" exists both inside the container (at /home/hnn_user/hnn) and outside (in the directory where step 3 was run) that can be used to share files between the container and your host OS.
   * If you run into problems starting the Docker container or the GUI is not displaying, please see the [Docker troubleshooting section](../docker/README.md#Troubleshooting)
   * If you closed the HNN GUI, and would like to restart it, run the following:
      ```
      docker-compose restart
      ```
5. **NOTE:** You may want run commands or edit files within the container. To access a command prompt in the container, use [`docker exec`](https://docs.docker.com/engine/reference/commandline/exec/):
    ```
    C:\Users\myuser>docker exec -ti mac_hnn_1 bash
    hnn_user@054ba0c64625:/home/hnn_user$
    ```

    If you'd like to be able to copy files from the host OS without using the shared directory, you do so directly with [`docker cp`](https://docs.docker.com/engine/reference/commandline/cp/).

## Method 2: native install

See the instructions in the file [mac-install-instructions.txt](mac-install-instructions.txt)