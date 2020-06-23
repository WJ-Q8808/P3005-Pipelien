pipeline {
    agent any
    stages {
       stage('Build') {
            steps {
              echo '编译'
              echo 'This is master branch..........'
              //sleep 10
            }
        }
       stage("代码编译与分析") {
            agent any
            steps {
               withSonarQubeEnv('ONES-Server') {
               sh ' sonar-scanner -Dsonar.projectKey=ONES-SonarQube-Projec -Dsonar.sources=.-Dsonar.login=9c8b59bef3f51834f0f0f2e83ab1669bbb8beb1c'
          }
        }
      }
   }
}
