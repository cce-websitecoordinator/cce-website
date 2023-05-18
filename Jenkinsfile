pipeline {
  agent any
  
  stages {
    stage('Clone repository') {
      steps {
        // Clone the repository using git
        git url: 'https://github.com/your/repo.git'
      }
    }
    
    stage('Build Docker image') {
      steps {
        // Build the Docker image using Dockerfile
        script {
          docker.build('your-image-name')
        }
      }
    }
    
    stage('Deploy to server') {
      steps {
        // Deploy the Docker image to your server
        script {
          docker.withRegistry('https://your-docker-registry', 'docker-credentials-id') {
            docker.image('your-image-name').push('production')
            // You can also perform additional deployment steps here, like restarting containers
          }
        }
      }
    }
  }
}
