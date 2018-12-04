FROM jenkins/jenkins:latest

#installs jenkins plugins
RUN /usr/local/bin/install-plugins.sh git mstest matrix-auth workflow-aggregator docker-workflow blueocean credentials-binding

#initializes environment variables to establish usernam and password for jenkins user
ENV JENKINS_USER admin
ENV JENKINS_PASS admin

# Skip initial setup wizard to avoid randomly generated password
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

#copies startup scripts into container
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/

VOLUME /var/jenkins_home
