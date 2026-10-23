
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out ITSM Ticket API source code'
                checkout scm
            }
        }

        stage('Verify Source Files') {
            steps {
                sh '''
                    test -f app/app.py
                    test -f app/requirements.txt
                    test -f app/test_app.py
                    test -f docker/Dockerfile
                '''
            }
        }

        stage('Python Syntax Check') {
            steps {
                sh '''
                    python3 -c "import ast; ast.parse(open('app/app.py').read())"
                    python3 -c "import ast; ast.parse(open('app/test_app.py').read())"
                    echo "Python syntax checks passed"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r app/requirements.txt
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    .venv/bin/python -m unittest app.test_app -v
                '''
            }
        }
        stage('Docker Build') {
            steps {
                sh '''
                    docker build \
                        -f docker/Dockerfile \
                        -t itsm-ticket-api:v1 .
                '''
            }
        }
    }
}