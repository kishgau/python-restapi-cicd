pipeline {
  agent { docker { image 'python:3.7.2' } }
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
  }
}
