pipeline{
  //not sure it will work :/
	agent any;

	stages{

		
		stage('Clone'){
			steps{
				git branch: 'main', url: 'git@github.com:mahmoudrd/JenkinsTask.git'
			}
		}
		
		
		stage('run'){
			steps{
        
				sh 'JENKINS_NODE_COOKIE=do_not_kill python3 -m ynet &'
        
			}
		}

		stage('slack sending'){
			steps{
				slackSend channel: '#breakingnews', message: 'here we go!'
			}
		}
	}
}
