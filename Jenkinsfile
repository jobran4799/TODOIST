pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                // Checkout SCM
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Selenium
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install selenium
                '''
                // Download and extract ChromeDriver using curl
                sh 'curl -O https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip'
                sh 'unzip chromedriver_linux64.zip -d /usr/local/bin/'
                sh 'rm chromedriver_linux64.zip'
                // Verify ChromeDriver installation
                sh 'chromedriver --version'
            }
    }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                python3 -m pytest tests_example_run.py
                '''
            }
        }
    }
    post {
        always {
            echo 'Cleaning up'
            // Clean up any actions necessary after pipeline execution
            sh 'rm -rf venv'
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