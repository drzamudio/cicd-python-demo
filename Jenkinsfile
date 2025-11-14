def sendWebexNotification(String message) {
    def botToken = "YTUzNWY5MTEtZDNiYS00N2ZhLWIwZjAtM2ZlYjM4YTkzMjViMjdhY2VmYWMtODUz_P0A1_e58072af-9d57-4b13-abf7-eb3b506c964d"
    def roomId = "aHR0cHM6Ly9jb252LXIud2J4Mi5jb20vY29udmVyc2F0aW9uL2FwaS92MS9jb252ZXJzYXRpb25zLzk3OTEyZWMwLTg0ODAtMTFmMC04MzU2LTRiZTgwZjcwYjExYw==
"

    sh """
        curl -X POST \
        https://webexapis.com/v1/messages \
        -H "Authorization: Bearer ${botToken}" \
        -H "Content-Type: application/json" \
        -d '{ "roomId": "${roomId}", "text": "${message}" }'
    """
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest'
            }
        }
    }

    post {
        success {
            sendWebexNotification("Jenkins Build SUCCESS for cicd-python-demo")
        }
        failure {
            sendWebexNotification("Jenkins Build FAILED for cicd-python-demo")
        }
    }
}
