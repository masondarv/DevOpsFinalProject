import jenkins.model.*

//does not allow builds to run on jenkins master
Jenkins.instance.setNumExecutors(0)
