pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        
    stage('Build Docker Images'){
      steps {
                sh'cd Bibliotheque_Numerique/backend/gestion_emprunt && docker build -t gestion_emprunt .'
                sh'cd Bibliotheque_Numerique/backend/gestion_livre && docker build -t gestion_livre .'
                sh'cd Bibliotheque_Numerique/backend/gestion_user && docker build -t gestion_user .'
                sh'cd Bibliotheque_Numerique/frontend && docker build -t frontend .'
            }

    }

    stage('Push Docker Images') {
          steps {
                sh'docker tag gestion_emprunt:latest lucifer92i/gestion_emprunt:latest'
                sh'docker tag gestion_livre:latest lucifer92i/gestion_livre:latest'
                sh'docker tag gestion_user:latest lucifer92i/gestion_user:latest'
                sh'docker tag frontend:latest lucifer92i/frontend:latest'

                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                sh'docker push lucifer92i/gestion_emprunt:latest'
                sh'docker push lucifer92i/gestion_livre:latest'
                sh'docker push lucifer92i/gestion_user:latest'
                sh'docker push lucifer92i/frontend:latest'
               
            }
            
    }
    }
    
    stage('Deploy'){
      steps {
                sh'cd Bibliotheque_Numerique && docker compose down '
                sh'cd Bibliotheque_Numerique && docker compose up -d --build'
            }

    }
}
}