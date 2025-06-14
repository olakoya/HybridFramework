pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest tests/ --html=reports/result.html'
      }
    }
  }

  post {
    success {
      archiveArtifacts artifacts: 'reports/*.html', fingerprint: true

      publishHTML(target: [
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'reports',
        reportFiles: 'result.html',
        reportName: 'Test Report'
      ])

      sh '''
        git config user.email "jenkins@example.com"
        git config user.name "Jenkins CI"
        git add reports/*.html
        git commit -m "Add test report for build ${BUILD_NUMBER}" || echo "Nothing to commit"
        git push origin HEAD:main
      '''
    }
  }
}
