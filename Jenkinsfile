pipeline {
    agent any

    stages {
      stage("Checkout"){
          steps {
              checkout([$class: 'GitSCM', 
                        branches: [[name: '*/master']], 
                        extensions: [], 
                        userRemoteConfigs: [[ url: 'https://github.com/krzysztofmarchewka/SimpleTestCI.git']]
                        ])
          }
        }
      stage("Version"){
          steps {
            echo 'Install dependencies'
              sh """
              python --version
              """
        }
      stage("build"){
          steps {
            echo 'Install dependencies'
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
}
