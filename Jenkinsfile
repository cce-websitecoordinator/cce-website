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
        script {
            def containerStatus = sh(returnStdout: true, script: 'docker inspect -f {{.State.Status}} cce-website-web-1').trim()
            if (containerStatus && containerStatus == 'running') {
                sh 'docker stop cce-website-web-1'
            }
            sh 'docker rm -f cce-website-web-1'

            def imageExists = sh(returnStatus: true, script: 'docker image inspect cce-website-web > /dev/null 2>&1').trim()
            if (imageExists == 0) {
                sh 'docker rmi -f cce-website-web'
            }
        }
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
