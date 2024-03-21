pipeline {
    agent any



    stages {
        stage('Setup Environment') {
            steps {
                echo '$path'
                echo 'Setting up Python environment...'
                bat 'C:\\Python\\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe tests_example_run.py"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "rd /s /q venv"
        }

        success {
            echo 'Build succeeded.'
            // Additional steps for successful build
        }

        failure {
            echo 'Build failed.'
            // Additional steps for failed build
        }
    }
}

//pipeline {
//    agent any

//    environment {
        // Define the Docker image name
//        IMAGE_NAME = 'tests'
//        TAG = 'latest'
//    }

//    stages {
//        stage('Build Docker Image') {
//            steps {
//                script {
//                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
//               }
//            }
//        }
//        stage('Setup Selenium Server HUB') {
//            steps {
//                echo 'Setting up Selenium server HUB...'
 //               bat "start /B java -jar selenium-server.jar hub"
 //               // Delay for 10 seconds
 //               bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
 //           }
 //       }

 //      stage('Setup Selenium Server nodes') {
 //           steps {
 //               echo 'Setting up Selenium server nodes...'
 //               bat "start /B java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
 //               // Delay for 10 seconds
 //               bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
 //           }
 //      }

 //       stage('Run Tests in Parallel') {
 //           steps {
 //               script {
 //                   parallel(
 //                       'API Test': {
 //                           bat "docker run --name tests_example_run ${IMAGE_NAME}:${TAG} python tests_example_run.py"
 //                           bat "docker rm tests_example_run"
 //                       },
 //                       'tests_example_run': {
 //                           bat "docker run --name Test_Runer ${IMAGE_NAME}:${TAG} python Test_Runer.py"
 //                           bat "docker rm Test_Runer"
 //                       }
 //                   )
 //               }
 //           }
 //       }
 //   }

 //   post {
 //       always {
 //           echo 'Cleaning up...'
 //           bat "docker rmi ${IMAGE_NAME}:${TAG}"
 //       }
 //   }
//}