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

        stage('Run API Test') {
            steps {
                bat "docker run --name api_tasks_tests ${IMAGE_NAME}:${TAG} python api_tasks_tests.py"
                bat "docker rm api_tasks_tests"
            }
        }

        stage('Run UI Test') {
            steps {
                bat "docker run --name tests_example_run ${IMAGE_NAME}:${TAG} python tests_example_run.py"
                bat "docker rm tests_example_run"
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