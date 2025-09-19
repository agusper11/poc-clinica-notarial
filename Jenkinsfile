pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/agusper11/poc-clinica-notarial.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Construye la imagen sin cache para asegurarnos que usa el último código
                sh 'docker build --no-cache -f backend/Dockerfile -t clinica-notarial:latest backend'
            }
        }

        stage('Run Container') {
            steps {
                // Detiene y elimina si ya existía, luego levanta el contenedor nuevo
                sh '''
                    docker stop clinica-notarial || true
                    docker rm clinica-notarial || true
                    docker run -d --name clinica-notarial -p 5000:5000 clinica-notarial:latest
                '''
            }
        }

        stage('Test App') {
            steps {
                // Verifica que el contenedor responde correctamente al endpoint raíz
                sh 'sleep 5 && curl -f http://localhost:5000 || exit 1'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker stop clinica-notarial || true && docker rm clinica-notarial || true'
            }
        }
    }
}
