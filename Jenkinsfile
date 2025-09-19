pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Obtiene el código del repositorio
                git branch: 'main', url: 'https://github.com/agusper11/poc-clinica-notarial.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Construye la imagen usando el Dockerfile en backend/
                sh 'docker build -f backend/Dockerfile -t clinica-notarial:latest backend'
            }
        }

        stage('Run Container') {
            steps {
                // Levanta el contenedor en segundo plano
                sh 'docker run -d --name clinica-notarial -p 5000:5000 clinica-notarial:latest || true'
            }
        }

        stage('Test App') {
            steps {
                // Verifica que el contenedor responde (saludo de Flask)
                sh 'sleep 5 && curl -f http://localhost:5000 || exit 1'
            }
        }

        stage('Cleanup') {
            steps {
                // Elimina el contenedor después de la prueba
                sh 'docker stop clinica-notarial || true && docker rm clinica-notarial || true'
            }
        }
    }
}
