pipeline {
  agent any

  environment {
    ECR_REGISTRY = '123456789012.dkr.ecr.us-east-1.amazonaws.com'
    ECR_REPOSITORY = 'my-ecr-repo'
    IMAGE_TAG = 'latest'
  }

  stages {
    stage('Deploy') {
      steps {
        script {
          withCredentials([[
              credentialsId: 'aws-ecr-creds',
              accessKeyVariable: 'AWS_ACCESS_KEY_ID',
              secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
          ]]) {
            sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ECR_REGISTRY"
            sh "docker pull $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"
            sh "docker run -d -p 8000:8000 $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"
          }
        }
      }
    }
  }
}
