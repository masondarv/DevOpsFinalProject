node('docker') {

    stage 'Checkout'
        checkout scm

    stage 'Build & UnitTest'
    sh "set -e"
    sh "docker-compose -f docker-compose.unit1.yml up"
    sh "docker-compose -f docker-compose.unit2.yml up"

    stage 'Integration Test'
    sh "set -e"
    sh "docker-compose -f docker-compose.int.yml up"

}
