pipeline {
  agent any
  stages {
    stage("Build") {
      steps {
        sh '''
        echo "Starting build"
        if `ls Dockerfile &> /dev/null`; then
          echo "Building Docker Image..."
          docker build -t julinux/django-gestao-app:latest .
        fi
        '''
      }
    }
  }
  post {
    success {
      sh 'docker rmi --force julinux/django-gestao-app:latest'
    }
  }
}
