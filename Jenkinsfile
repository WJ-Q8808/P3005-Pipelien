pipeline {
   agent any
   environment {
       BranchName="master"
   }
   stages {
      stage('Start build') {
         steps {
            echo 'pwd'
            //sleep 360
            sleep 10
            //dir('/var/jenkins_home/workspace') {
               //sh 'ps'
            //}
            echo 'Build runing1'
            sh "ps -a"
         }
      }
      stage('Code review'){
         steps {
           echo "This is Codeing......"
           //sleep 15
           sh "pwd"
           echo "runing master"
           //sleep 15
         }
      }
      stage('Test runing'){
         when {
            branch 'master'
         }
         steps {
           //sleep 360
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
