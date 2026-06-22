pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                checkout scm
            }
        }
        
        stage('Data Quality Check') {
            steps {
                echo 'Running pre-flight checks...'
                bat 'python --version'
            }
        }
        
        stage('Run ETL Pipeline') {
            steps {
                echo 'Executing Python data processor...'
                bat 'python process_data.py'
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                echo 'Saving the processed dataset...'
                archiveArtifacts artifacts: 'output/clean_data.json', followSymlinks: false
            }
        }
    }
}