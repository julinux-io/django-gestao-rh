pipeline {
  agent any
  stages {
    stage("Pre-Build") {
      steps {
        sh 'env'
      }
    }
    stage("Build") {
      agent {
        docker {
        image 'python:3.9.10'
    }
      }
      steps {
        sh 'pip3 install pipenv'
        sh 'pipenv install'
      }
    }
  }
}
