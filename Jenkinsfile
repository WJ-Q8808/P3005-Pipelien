pipeline {
    agent any
    stages {
       stage('Build') {
          parallel{
              stage('单元测试'){
                 steps {
                    sleep 20
                    echo 'Build Module1--01 stage'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                sleep 30
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                sleep 40
                echo 'Deploying....'
            }
        }
    }
}
