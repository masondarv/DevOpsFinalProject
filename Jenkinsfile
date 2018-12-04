//selects docker as the build agent
node('docker') {

    stage 'Checkout'
        checkout scm

    stage('Build & UnitTest') {
      // build and unit test Budget class
      sh "docker-compose -f docker-compose.unit1.yml up"
      rv1 = sh (returnStdout: true, script: "docker inspect c1 --format='{{.State.ExitCode}}'").trim()
      echo "return value of budget class test is ${rv1}"

      //build and unit test Expense class
      sh "docker-compose -f docker-compose.unit2.yml up"
      rv2 = sh (returnStdout: true, script: "docker inspect c2 --format='{{.State.ExitCode}}'").trim()
      echo "return value of expense class test is ${rv2}"

      if (rv1 != '0' || rv2 != '0') {
        sh "exit 1"
        } else {
        echo "Unit tests passed"
        }
      }

    stage('Integration Test') {
      //build both classes and run an integration test
      sh "docker-compose -f docker-compose.int.yml up"
      rv3 = sh (returnStdout: true, script: "docker inspect int --format='{{.State.ExitCode}}'").trim()
      echo "return value of integration test is ==> ${rv3}"

      if (rv3 != '0') {
        sh "exit 1"
        } else {
        echo "Integration tests passed"
        }
    }

}
