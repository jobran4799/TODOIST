pipeline {
    agent any

    environment {
        PIP_PATH = 'C:\Users\pc-admin\AppData\Local\Programs\Python\Python312\python.exe'
        PYTHON_PATH = 'C:\Users\pc-admin\AppData\Local\Microsoft\WindowsApps\python.exe'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo '$path'
                echo 'Setting up Python environment...'
                bat 'C:\Users\pc-admin\AppData\Local\Programs\Python\Python312\python.exe -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
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
                bat "venv\\Scripts\\python.exe -m unittest tests/API/api_tasks_tests.py"
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