pipeline {
    agent any
    parameters {
      choice(name: 'VERSION', choices: ['1.0','1.1','1.1.2'],description: 'Choose the version for build execution')
      booleanParam(name:'executeTests', defaultValue: true, description: 'Test execution')
    }

    stages {
<<<<<<< HEAD
      stage("checkout the branch inside the pipeline"){
=======
      stage("checkout"){
>>>>>>> 1e8b166b8434119bf288f472ace71812dc948ac6
          steps {
              checkout([$class: 'GitSCM', 
                        branches: [[name: '*/master']], 
                        extensions: [], 
                        userRemoteConfigs: [[ url: 'https://github.com/krzysztofmarchewka/SimpleTestCI.git']]
                        ])
          }
        }
    stage("build"){
<<<<<<< HEAD
=======
      agent {
          docker {
            image 'python:3.12.0-alpine3.18'
          }
            }
>>>>>>> 1e8b166b8434119bf288f472ace71812dc948ac6
      steps {
          echo 'Check python version'
          sh 'python --version'
          echo 'Install requirements'
          sh 'pip install -r requirements.txt'  
        }
    }
    stage("test"){
<<<<<<< HEAD
=======
      agent {
          docker {
            image 'python:3.12.0-alpine3.18'
          }
            }
>>>>>>> 1e8b166b8434119bf288f472ace71812dc948ac6
      steps {
          echo 'Run the tests' 
          sh 'python app/main_test.py'
        }
      }
    }
<<<<<<< HEAD
  }
=======
  }
>>>>>>> 1e8b166b8434119bf288f472ace71812dc948ac6
