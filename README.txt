Steps to Setup and Execute CI/CD pipeline using Docker+Jenkins

1) From ./FinalProject run "vagrant up" to launch the VM that will run docker and jenkins.

2) run "vagrant ssh adm" to ssh into the VM.

2) From the command line, run "cd /vagrant/jenkins-docker/master" to navigate to the folder with the folder used to build the jenkins master

3) From the command line, run "sudo docker build -t jenkins-master ."

4) From the command line, run "cd /vagrant/jenkins-docker/slave" to navigate to the folder with the folder used to build the jenkins slave

5) From the command line, run "sudo docker build -t jenkins-slave ."

6) From the command line, run "cd /vagrant"

7) From the command line, run "docker-compose -f docker-compose.ci.yml up" to launch the Jenkins infrastructure

8) Open a web browser and access the Jenkins web UI at  http://192.168.33.10:8080

