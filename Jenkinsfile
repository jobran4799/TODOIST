pipeline {
    agent any

    stages {
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                // Download Selenium Server JAR
                sh 'curl -O https://selenium-release.storage.googleapis.com/4.0-beta-4/selenium-server-4.0.0-beta-4.jar'
                // Start Selenium Server HUB
                sh 'java -jar selenium-server-4.0.0-beta-4.jar hub &'
                // Delay for 10 seconds
                sh 'sleep 10'
            }
        }

        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                // Start Selenium Server Node
                sh 'java -jar selenium-server-4.0.0-beta-4.jar node --port 5555 --selenium-manager true &'
                // Delay for 10 seconds
                sh 'sleep 10'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Run your tests here
                sh 'python tests_example_run.py'
                sh 'python Test_Runer.py'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // You can add cleanup steps here if needed
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