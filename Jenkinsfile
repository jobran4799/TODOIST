pipeline {
    agent any

    stages {
        stages {
            stage('Setup') {
                steps {
                    // Set up any necessary environment
                    sh 'python -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }

            stage('Run Tests') {
                steps {
                    // Run pytest tests
                    sh 'pytest Main_page_pytest.py --html=report.html'
                }
            }

            stage('Publish HTML Report') {
                steps {
                    // Archive HTML report as a build artifact
                    archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: true

                    // Publish HTML report (optional, requires Jenkins HTML Publisher plugin)
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: false,
                        reportDir: '',
                        reportFiles: 'report.html',
                        reportName: 'HTML Test Report'
                    ])
                }
            }
        }

        post {
            always {
                // Clean up any resources if necessary
            }
        }
    }
}
