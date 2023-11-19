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
    stage("install"){
          steps {
            echo 'Install Python'
              sh """
              apt install python
              """
        }
      } 
      stage("version"){
          steps {
            echo 'Check Python version'
              sh """
              python --version
              """
        }
      }
      stage("build"){
          steps {
            echo 'Install requirements'
              sh """
              pip install -r requirements.txt
              """
        }
      }
      stage("test"){
          steps {
             echo 'Run the tests' 
              sh """
              python app/main_test.py
              """
        }
      }
      stage("run"){
          steps {
            echo 'Run the app'
              sh """
              python app/main.py
              """
        }
      }
    }
  }
