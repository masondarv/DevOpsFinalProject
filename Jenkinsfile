node('docker') {

    stage 'Checkout'
        checkout scm

    stage 'Build & UnitTest'
    sh 'docker-compose -f docker-compose.unit1.yml up'
    sh (returnStdout: true, script: 'docker inspect class1 --format='{{.State.ExitCode}}')
    sh 'docker-compose -f docker-compose.unit2.yml up'
    sh (returnStdout: true, script: 'docker inspect class2 --format='{{.State.ExitCode}}')

    stage 'Integration Test'
    sh (returnStatus: true, script: 'docker-compose -f docker-compose.int.yml up')
    sh (returnStdout: true, script: 'docker inspect integration --format='{{.State.ExitCode}}')

}
