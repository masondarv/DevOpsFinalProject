import jenkins.model.*
import hudson.security.*

//gets system environment variables
def env = System.getenv()

//creates an instance of the jenkins master
def jenkins = Jenkins.getInstance()

//security realm determines users and passwords, as well as what groups the users belong to
jenkins.setSecurityRealm(new HudsonPrivateSecurityRealm(false))

//determines which users can access what
jenkins.setAuthorizationStrategy(new GlobalMatrixAuthorizationStrategy())

//adds user to jenkins security realm
def user = jenkins.getSecurityRealm().createAccount(env.JENKINS_USER, env.JENKINS_PASS)
user.save()

// gives Jenkins user global access
jenkins.getAuthorizationStrategy().add(Jenkins.ADMINISTER, env.JENKINS_USER)
jenkins.save()
