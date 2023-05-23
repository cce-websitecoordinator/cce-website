/* groovylint-disable-next-line CompileStatic */
pipeline {
  agent any
  environment {
    AWS_ACCOUNT_ID = '435034921146'
    AWS_DEFAULT_REGION = 'ap-south-1'
    IMAGE_REPO_NAME = 'website'
    REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    registryCredential = 'websitecoordinator'
  }

  stages {
    stage('Stop Containers and Remove Image') {
      steps {
        sh 'docker stop cce-website-web-1'
        sh 'docker rm cce-website-web-1'
        sh 'docker rmi -f  cce-website-web'
      }
    }

      stage('Pull from Git') {
      steps {
        sh "cd cce-website  && git pull origin production"
      }
      }
    stage('Deploy') {
      steps {
        sh 'sudo docker-compose up -d '
      }
    }
  }
}
