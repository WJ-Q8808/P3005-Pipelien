pipeline {
   agent any
   environment {
       BranchName="F2048"
   }
   stages {
      stage('Start build') {
         steps {
            echo 'pwd'
            //sleep 360
            //dir('/var/jenkins_home/workspace') {
               //sh 'ps'
            //}
            echo 'Build runing'
            sh "pwd"
         }
      }
      stage("代码编译与分析") {
            steps {
              withSonarQubeEnv('ONES-Server') {
                sh '-Dsonar.projectKey=JenkinsSonarqube -Dsonar.python.binaries=.'
              }
              script {
                def qg = waitForQualityGate()
                println qg.status
             }
         }
      }
      stage('Code review'){
         steps {
           echo "This is Codeing......"
           echo "1runing master"
         }
      }
      stage('Test runing'){
         when {
            branch 'F2048'
         }
         steps {
           echo "Test master"
         }
      }
      stage('Deploy ending') {
         environment {Description="This is "}
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/F2048'){
                  echo "${Description}${BranchName}"
                  sh "ls"
               }
            }
         }
      }
    }
}
