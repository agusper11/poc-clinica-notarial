pipeline {
    agent any

    environment {
        IMAGE_NAME = "clinica-notarial:latest"
        CONTAINER_NAME = "clinica-test"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/agusper11/poc-clinica-notarial.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Docker') {
            steps {
                sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                sh "sleep 5" // Espera que el contenedor esté listo
            }
        }

        stage('Test') {
            steps {
                sh "curl http://localhost:5000"
            }
        }

        stage('Clean up') {
            steps {
                sh "docker stop ${CONTAINER_NAME}"
                sh "docker rm ${CONTAINER_NAME}"
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado"
        }
    }
}
