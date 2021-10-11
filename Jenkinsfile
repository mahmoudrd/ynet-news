pipeline{
  //not sure it will work :/
	agent any;

	stages{

		
		stage('clone'){
			steps{
				git branch: 'main', url: 'https://github.com/mahmoudrd/ynet-news.git'
			}
		}
		
		
		stage('run'){
			steps{
        
				sh 'JENKINS_NODE_COOKIE=do_not_kill python3 -m ynet &'
        
			}
		}

		stage('slack sending'){
			steps{
				slackSend channel: '#breakingnews', message: 'we are up!'
			}
		}
	}
}
