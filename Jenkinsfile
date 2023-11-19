pipeline {
    agent any

    stages {
      stage("checkout"){
          steps {
              checkout([$class: 'GitSCM', 
                        branches: [[name: '*/master']], 
                        extensions: [], 
                        userRemoteConfigs: [[ url: 'https://github.com/krzysztofmarchewka/SimpleTestCI.git']]
                        ])
          }
        }
    stage("build"){
      agent {
          docker {
            image 'python:3.12.0-alpine3.18'
          }
            }
      steps {
          echo 'Check python version'
          sh 'python --version'
          echo 'Install requirements'
          sh 'pip install -r requirements.txt'  
        }
    }
    stage("test"){
      agent {
          docker {
            image 'python:3.12.0-alpine3.18'
          }
            }
      steps {
          echo 'Run the tests' 
          sh 'python app/main_test.py'
        }
      }
    }
  }
