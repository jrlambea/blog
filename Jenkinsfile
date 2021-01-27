pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                sh 'echo "Nothing to see here :D"'
                sh '''
                    echo "Maybe in a future we can implement 'pelican content' here."
                    ls -lah
                   '''
            }
	    }
        stage('Lint HTML') {
            steps {
                sh 'echo "Do not check anything. Only for test purposes."'
                sh 'echo "tidy -e -q output/*.html"'
            }
        }
        stage('Upload to AWS') {
            steps {
                withAWS(region:'eu-west-1',credentials:'aws-credentials') {
                s3Upload(pathStyleAccessEnabled:true, payloadSigningEnabled: true, file:'output/', bucket:'jrlambea.me')
                // s3Upload(pathStyleAccessEnabled:true, payloadSigningEnabled: true, file:'', bucket:'jrlambea.me')
                }
            }
        }
        stage('Check Online') {
            steps {
                sh 'curl https://jrlambea.me > /dev/null'
            }
        }
    }
}
