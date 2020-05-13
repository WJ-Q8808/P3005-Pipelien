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
            //sleep 30
            //dir('/var/jenkins_home/workspace') {
               //sh 'ps'
            //}
            echo 'Build runing'
            sh "ps -a"
         }
      }
      stage('Code review'){
         steps {
           echo "This is Codeing......"
           //sleep 15
           sh "pwd"
           echo "runing master"
           //sh "pwd"
         }
      }
      stage('Test runing'){
         when {
            branch 'F2048'
         }
         steps {
           //sleep 15
           echo "runing master"
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
   }
}
