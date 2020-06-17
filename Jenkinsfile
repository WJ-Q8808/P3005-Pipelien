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
            //sleep 21
            //dir('/var/jenkins_home/workspace') {
               //sh 'ps'
            //}
            echo 'Build runing'
            sh "pwd"
         }
      }
      stage('Code review'){
         steps {
           echo "This is Codeing......"
           //sleep 30
           //sleep 15
           echo "1runing master"
           //sh "python3 Count_date.py"
         }
      }
      stage('Test runing'){
         when {
            branch 'F2048'
         }
         steps {
           //sleep 15
           echo "Test master"
         }
      }
      stage('Deploy ending') {
         environment {Description="This is "}
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/F2048'){
                  echo "${Description}${BranchName}"
                  //sleep 25
                  sh "ls"
               }
            }
         }
      }
      stage('build && SonarQube analysis') {
         steps {
            withSonarQubeEnv('WuJianSonarQuebeServers') {
               sh '/var/lib/jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/MySonarQubeScanner/bin/sonar-scanner'
              }
           }
        }
      }
   }
}
