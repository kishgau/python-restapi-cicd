pipeline {
  agent { 
       docker { 
           image 'python:3.7.2' 
           args '--user 0:0' 
       }
  }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install --no-cache-dir -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
    stage('CleanWorkspace') {
         steps {
          cleanWs()
          }

  }


}
