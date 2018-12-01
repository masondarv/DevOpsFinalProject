node('docker') {

    stage 'Checkout'
        checkout scm
    stage 'Build & UnitTest'
    sh "docker-compose up -d"
      
}
