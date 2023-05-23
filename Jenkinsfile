pipeline {
  agent any
  environment {
    AWS_ACCOUNT_ID="435034921146"
    AWS_DEFAULT_REGION="ap-south-1"
    IMAGE_REPO_NAME="website"
    IMAGE_TAG=”${env.BUILD_ID}”
    REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    registryCredential = "websitecoordinator"
  
  }

  stages {
    stage('Build') {
      steps {
        echo 'Building..'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}


