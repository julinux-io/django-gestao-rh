pipeline {
  agent any
  environment {
    CI = 'true'
  }
  stages {
    stage("build") {
      steps {
          script {
            cache(maxCacheSize: 5000, caches: [
              [$class: 'ArbitraryFileCache', excludes: '', includes: 'latest.tar', path: '']
            ]) {
            sh '''
              if [ -f latest.tar ]; then
                docker image load -i latest.tar
              fi
              if `ls Dockerfile &> /dev/null`; then
                echo "Building Docker Image..."
                docker build -t julinux/django-gestao-app:${BUILD_NUMBER} .
                docker image save -o latest.tar julinux/django-gestao-app:${BUILD_NUMBER}
              fi
            '''
          }
        }
      }
    }
  }
  post {
    success {
      sh 'docker rmi --force julinux/django-gestao-app:${BUILD_NUMBER}'
      sh 'rm -rf latest.tar'
    }
  }
}
