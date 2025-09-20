pipeline {
    agent any

    environment {
        IMAGE_NAME = "clinica-notarial:${BRANCH_NAME}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checkout branch: ${BRANCH_NAME}"
                git branch: "${BRANCH_NAME}", url: 'https://github.com/agusper11/poc-clinica-notarial.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image for ${BRANCH_NAME}"
                sh "docker build -f backend/Dockerfile -t ${IMAGE_NAME} backend"
            }
        }

        stage('Run Container') {
            steps {
                echo "Running container for ${BRANCH_NAME}"
                sh """
                    docker rm -f clinica-notarial-${BRANCH_NAME} || true
                    docker run -d --name clinica-notarial-${BRANCH_NAME} -p 5000:5000 ${IMAGE_NAME}
                """
            }
        }

        stage('Test App') {
            steps {
                echo "Testing application in branch ${BRANCH_NAME}"
                sh 'sleep 5 && curl -f http://localhost:5000/ || exit 1'
            }
        }

        stage('Optional Cleanup') {
            steps {
                echo "Stopping container for ${BRANCH_NAME} (optional)"
                // Comenta la siguiente línea si querés mantener el contenedor levantado
                sh "docker stop clinica-notarial-${BRANCH_NAME} || true && docker rm clinica-notarial-${BRANCH_NAME} || true"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished for branch ${BRANCH_NAME}"
        }
    }
}
