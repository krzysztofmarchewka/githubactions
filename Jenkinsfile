pipeline {
    agent any
    parameters {
      choice(name: 'VERSION', choices: ['1.0','1.1','1.1.2'],description: 'Choose the version for build execution')
      booleanParam(name:'executeTests', defaultValue: true, description: 'Test execution')
    }

    stages {
      stage("checkout the branch inside the pipeline"){
          steps {
              checkout([$class: 'GitSCM', 
                        branches: [[name: '*/master']], 
                        extensions: [], 
                        userRemoteConfigs: [[ url: 'https://github.com/krzysztofmarchewka/SimpleTestCI.git']]
                        ])
          }
        }
    stage("build"){
      steps {
          echo 'Check python version'
          sh 'python --version'
          echo 'Install requirements'
          sh 'pip install -r requirements.txt'  
        }
    }
    stage("test"){
      steps {
          echo 'Run the tests' 
          sh 'python app/main_test.py'
        }
      }
    }
  }