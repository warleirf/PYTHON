#!/bin/bash
yum update -y
yum upgrade -y
amazon-linux-extras install docker git -y
sudo yum install docker git -y
sudo usermod -a -G docker ec2-user
id ec2-user
# Reload a Linux user's group assignments to docker w/o logout
newgrp docker
wget https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)
sudo mv docker-compose-$(uname -s)-$(uname -m) /usr/local/bin/docker-compose
sudo chmod -v +x /usr/local/bin/docker-compose
sudo systemctl enable docker.service
sudo systemctl start docker.service
# Getting docker version info on Amazon Linux
echo "$PATH"
export PATH=$PATH:/usr/local/bin
sudo find / -name "docker-compose" -ls
docker version
docker-compose version