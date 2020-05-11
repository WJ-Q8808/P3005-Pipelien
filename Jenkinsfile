pipeline {
   agent any
   environment {
       BranchName="Newmaster2"
   }
   stages {
      stage('Start build') {
         steps {
            echo 'pwd'
            //sleep 360
            sleep 30
            //dir('/var/jenkins_home/workspace') {
               //sh 'ps'
            //}
            echo 'Build runing'
            sh "pwd"
         }
      }
      stage('Code Review'){
         steps {
           echo "This is Codeing......"
           sleep 15
           //sh "ls -l"
           //sh "pwd"
           echo "runing master"
         }
      }
      stage('Test Runing'){
         when {
            branch 'master'
         }
         steps {
           //sleep 15
           echo "runing master"
         }
      }
      stage('Run Ending') {
         environment {Description="This is "}
         steps{
            script{
               if (env.GIT_BRANCH == 'origin/Newmaster2'){
                  echo "${Description}${BranchName}"
                  //sleep 25
                  sh "ls"
               }
            }
         }
      }
   }
}
