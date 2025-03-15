pipeline {
    agent any

    environment {
        IMAGE_NAME = 'malinam/worldofgames-flask-app'  // Replace with your Docker Hub username and app name
        CONTAINER_NAME = 'flask-app'
        DOCKER_TAG = 'latest'
        SCORE_FILE = 'Scores.txt'  // Path to the dummy Scores.txt file
        COMPOSE_FILE = 'docker-compose.yml'  // Path to your docker-compose.yml file
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Build the Docker image using Docker Compose
                    echo "Building the Docker image with docker-compose..."
                    sh """
                        docker-compose -f ${COMPOSE_FILE} build
                    """
                }
            }
        }
        
        
        stage('Run') {
            steps {
                script {
                    // Ensure the container is stopped and removed if it exists
                    echo "Starting the Dockerized application with docker-compose..."

                    // Stop and remove any existing container
                    sh """
                        docker-compose -f ${COMPOSE_FILE} down || true
                    """

                    // Run the container with docker-compose
                    sh """
                        docker-compose -f ${COMPOSE_FILE} up -d
                    """
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run the Selenium tests (e2e.py) against the running container
                    echo "Running tests with Selenium..."

                    // Ensure Python environment is available
                    sh 'pip install -r requirements.txt'

                    // Run the e2e.py script
                    sh 'python e2e.py'  // Adjust the command to how you run the Selenium tests

                    // Fail the pipeline if tests fail
                }
            }
        }
        
        stage('Finalize') {
            steps {
                script {
                    // Terminate the tested container and clean up
                    echo "Stopping and cleaning up Docker containers..."

                    // Stop and remove the container
                    sh """
                        docker-compose -f ${COMPOSE_FILE} down
                    """

                    // Push the new image to Docker Hub
                    echo "Pushing the image to Docker Hub..."
                    sh "docker push ${IMAGE_NAME}:${DOCKER_TAG}"
                }
            }
        }
        
    }
    
    post {
        always {
            // Clean up docker resources to ensure the system is clean for the next run
            echo "Cleaning up Docker images..."
            sh "docker system prune -f"
        }

        success {
            echo "Pipeline succeeded!"
        }

        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}