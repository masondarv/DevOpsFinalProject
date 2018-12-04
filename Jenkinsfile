node('docker') {

    stage 'Checkout'
        checkout scm

    stage 'Build & UnitTest'
    sh (returnStatus: true, script: 'docker-compose -f docker-compose.unit1.yml up')
    sh (returnStatus: true, script: 'docker-compose -f docker-compose.unit2.yml up')

    stage 'Integration Test'
    sh (returnStatus: true, script: 'docker-compose -f docker-compose.int.yml up')

}
