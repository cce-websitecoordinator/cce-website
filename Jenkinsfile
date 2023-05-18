pipeline {
  agent any

  stages {
    stage('Clone repository') {
      steps {
        // Clone the repository
        git url: 'https://github.com/cce-websitecoordinator/cce-website.git'
      }
    }

    stage('Build Docker image') {
      steps {
        // Build the Docker image
        script {
          docker.build('435034921146.dkr.ecr.ap-south-1.amazonaws.com/website')
        }
      }
    }

    stage('Tag and Push to ECR') {
      steps {
        // Authenticate Docker with ECR
        script {
          sh 'aws ecr get-login-password --region <aws-region> | docker login --username AWS --password-stdin 435034921146.dkr.ecr.ap-south-1.amazonaws.com/website'
        }

        // Tag the Docker image
        script {
          sh 'docker tag 435034921146.dkr.ecr.ap-south-1.amazonaws.com/website 435034921146.dkr.ecr.ap-south-1.amazonaws.com/website:latest'
        }

        // Push the Docker image to ECR
        script {
          sh 'docker push 435034921146.dkr.ecr.ap-south-1.amazonaws.com/website:latest'
        }
      }
    }

    stage('Pull image') {
      steps {
        // Pull the Docker image from ECR
        script {
          sh 'docker pull 435034921146.dkr.ecr.ap-south-1.amazonaws.com/website:latest'
        }
      }
    }

    stage('Deploy image') {
      steps {
       
        script {
            docker run -d -p 8080:8080 435034921146.dkr.ecr.ap-south-1.amazonaws.com/website:latest
         
        }
      }
    }
  }
}
