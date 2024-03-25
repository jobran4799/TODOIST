pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\Users\pc-admin\AppData\Local\Programs\Python\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Environment stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Environment stage failed.")
                }
            }
        }
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /b java -jar selenium-server-4.17.0.jar hub"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Selenium Server HUB stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Selenium Server HUB stage failed.")
                }
            }
        }
        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                bat "start /b java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true"
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Setup Selenium Server nodes stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Setup Selenium Server nodes stage failed.")
                }
            }
        }
        stage(' Running Tests') {
            steps {
                echo 'Testing..'
                bat "venv\\Scripts\\python.exe pytest Main_page_pytest.py --html=report.html"
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Running Tests stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Running Tests stage failed.")
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
            post {
                success {
                    slackSend (color: 'good', message: "SUCCESS: Deploy stage completed successfully.")
                }
                failure {
                    slackSend (color: 'danger', message: "FAILURE: Deploy stage failed.")
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // General cleanup notification
            slackSend (color: 'warning', message: "NOTIFICATION: Cleaning up resources...")
        }
        success {
            echo 'Build succeeded.'
            slackSend (color: 'good', message: "SUCCESS: Build completed successfully.")
        }
        failure {
            echo 'Build failed.'
            slackSend (color: 'danger', message: "FAILURE: Build failed.")
        }
    }
}