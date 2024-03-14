pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'API Test': {
                            bat "docker run --name api_parallel_tests ${IMAGE_NAME}:${TAG} python api_parallel_tests.py"
                            bat "docker rm api_parallel_tests"
                        },
                        'tests_example_run': {
                            bat "docker run --name Test_Runer ${IMAGE_NAME}:${TAG} python Test_Runer.py"
                            bat "docker rm Test_Runer"
                        }
                    )
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}