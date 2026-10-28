
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checkout completed.'
            }
        }

        
    stage('Build') {
        steps {
            bat '''
                if not exist "index.html" exit /b 1
                if not exist "style.css" exit /b 1
                if not exist "script.js" exit /b 1
                if not exist "test.py" exit /b 1
            '''
            echo 'Build check successful.'
        }
    }


        stage('Test') {
            steps {
                bat 'python --version'
                bat 'python -m unittest test.py'
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully!'
        }
        failure {
            echo 'Build or tests failed. Check Console Output.'
        }
    }
}
