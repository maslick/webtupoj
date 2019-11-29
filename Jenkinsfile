def branch
def revision
def registryIp
def buildName = "build-webtupoj"
def imageName = "webtupoy"
def registryName = "docker-registry.regionview.ru"

pipeline {
    agent {
        kubernetes {
            label "${buildName}-pod"
            defaultContainer 'jnlp'
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    job: build-service
spec:
  containers:
  - name: python
    image: python:3.7
    command: ["cat"]
    tty: true
  - name: docker
    image: docker:18.09.2
    command: ["cat"]
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }
    options {
        skipDefaultCheckout true
    }

    stages {
        stage ('checkout') {
            steps {
                script {
                    def repo = checkout scm
                    revision = sh(script: 'git log -1 --format=\'%h.%ad\' --date=format:%Y%m%d-%H%M | cat', returnStdout: true).trim()
                    branch = repo.GIT_BRANCH.take(20).replaceAll('/', '_')
                    if (branch != 'master') {
                        revision += "-${branch}"
                    }
                    sh "echo 'Building revision: ${revision}'"
                }
            }
        }
        stage ('build') {
            steps {
                container('docker') {
                    sh "docker build . -t ${imageName}:${revision}"
                }
            }
        }
        stage ('test') {
            steps {
                container('python') {
                    sh "pip3 install -r requirements.txt"
                    sh "python3 -m unittest discover applications/webtupoj/tests/unit"
                }
            }
        }
        stage ('publish artifact') {
            when {
                expression {
                    branch == 'develop' || branch == 'master'
                }
            }
            steps {
                container('docker') {
                    withCredentials([usernamePassword(credentialsId: 'docker_registry', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]){
                        sh "docker tag ${imageName}:${revision} ${registryName}/${imageName}:latest"
                        sh "docker tag ${imageName}:${revision} ${registryName}/${imageName}:${revision}"

                        sh "docker login ${registryName} --username $DOCKER_USERNAME --password $DOCKER_PASSWORD"
                        sh "docker push ${registryName}/${imageName}:latest"
                        sh "docker push ${registryName}/${imageName}:${revision}"
                    }
                }
            }
        }
    }
}
