pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Application') {
          steps {
                sh'cd  backend/gestion_emprunt && pip install -r requirements.txt'
                sh'cd  backend/gestion_livre && pip install -r requirements.txt'
                sh'cd  backend/gestion_user && pip install -r requirements.txt'
            }
            
    }
    stage('Build Docker Images'){
      steps {
                sh'cd backend/gestion_emprunt && docker build -t gestion_emprunt .'
                sh'cd backend/gestion_livre && docker build -t gestion_livre .'
                sh'cd backend/gestion_user && docker build -t gestion_user .'
                sh'cd frontend && docker build -t frontend .'
            }

    }
    stage('Deploy'){
      steps {
                sh'docker compose down '
                sh'docker compose up -d --build'
            }

    }
}
}