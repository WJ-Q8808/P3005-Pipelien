pipeline {
    agent any
    stages {
       stage('Build') {
             steps {
                echo '编译'
            }
        }
       stage('代码编译') {
          parallel {
            stage('代码分析01'){
                steps {
                   echo '代码分析ing...'
                  }
              }
            stage('代码分析02'){
                steps {
                   echo '集成测试ing...'
                   }
              }
            stage('代码分析03'){
                when {
                  branch "master"
               }
                steps {
                   echo '代码分析完成...'
                  }
               }
           }
       }
       stage('Test runing') {
          parallel {
            stage('单元测试'){
                when {
                   branch "master"
              }
                steps {
                   echo '单元测试ing...'
                  }
              }
            stage('接口测试'){
                steps {
                   echo '接口测试ing....'
                   }
              }
            stage('集成测试'){
                steps {
                   echo '集成测试ing...'
                  }
               }
           }
       }
       stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}