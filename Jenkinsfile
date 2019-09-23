pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:slim' 
                }
            }
            steps {
                sh 'python3 --version' 
            }
        }
    }
}
