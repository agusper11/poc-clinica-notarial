pipeline {
    agent any

    environment {
        // Reemplaza los slashes de la rama por guiones para usarlo como tag de Docker
        DOCKER_TAG = "${env.BRANCH_NAME.replaceAll('/', '-')}"
        IMAGE_NAME = "clinica-notarial:${DOCKER_TAG}"
        CONTAINER_NAME = "clinica-notarial-${DOCKER_TAG}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clona la rama actual
                git branch: "${env.BRANCH_NAME}", url: 'https://github.com/agusper11/poc-clinica-notarial.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Construye la imagen usando el Dockerfile de backend
                sh "docker build -f backend/Dockerfile -t ${IMAGE_NAME} backend"
            }
        }

        stage('Run Container') {
            steps {
                // Levanta el contenedor en segundo plano con nombre basado en la rama
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME} || true"
            }
        }

        stage('Test App') {
            steps {
                // Espera que arranque y prueba la app
                sh 'sleep 5 && curl -f http://localhost:5000 || exit 1'
            }
        }

        stage('Cleanup') {
            steps {
                // Detiene y elimina el contenedor después de la prueba
                sh "docker stop ${CONTAINER_NAME} || true && docker rm ${CONTAINER_NAME} || true"
            }
        }
    }

    post {
        always {
            // Asegura limpieza de cualquier contenedor residual
            sh "docker ps -a | grep ${CONTAINER_NAME} && docker rm -f ${CONTAINER_NAME} || true"
        }
    }
}
