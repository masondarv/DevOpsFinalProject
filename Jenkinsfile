node('docker') {

    stage 'Checkout'
        checkout scm

    stage 'Build & UnitTest'
    sh "sudo docker-compose -f docker-compose.unit.yml up"

    stage 'Integration Test'
    sh "sudo docker-compose -f docker-compuse.int.yml up"

}
