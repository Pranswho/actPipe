# Project VASP

## Jenkins Pipeline Script:

```
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                
                git branch: 'main', url: 'https://github.com/Pranswho/actPipe.git'
            }
        }
        stage('Build') {
            steps {
               
                bat 'python LinkedList.py build'
            }
        }
        stage('Test') {
            steps {
                // Run the test command
                bat 'python -m unittest UnitTesting.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}

```
![image](https://github.com/user-attachments/assets/81834e0c-3a66-4be3-a220-b720e00dcc94)

Team Members - Vridhi, Ayush, Sanskar, Pranshu
