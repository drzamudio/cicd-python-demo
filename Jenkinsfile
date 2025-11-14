pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/drzamudio/cicd-python-demo.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'py -3 -m unittest'
            }
        }
    }

    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
