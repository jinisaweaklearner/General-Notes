# Jenkins
Mainly, we use Jenkins for the reasons below:
- deploy infra via Terraform
- upload Airflow dag scripts to s3 bucket
- upload Glue ETL scripts to s3 bucket
- deploy docker images to ECS/ECR

- what is /usr/local/bin
https://stackoverflow.com/questions/43987005/jenkins-does-not-recognize-command-sh
- SCM = Source Control Management

### Interpolation via Jenkins
In the current project, we use Python scripts read the env.var file as a txt file and get values by "|" via Jenkins.

Another way is to set values with a .tfvars file https://learn.hashicorp.com/tutorials/terraform/sensitive-variables
GitHub's recommended .gitignore file for Terraform configuration is configured to ignore files matching the pattern *.tfvars


### Agent
An agent is typically a machine, or container, which connects to a Jenkins controller and executes tasks when directed by the controller.
```
agent{
  node{
    label 'master'
  }
}
```

### Stage
stage is part of Pipeline, and used for defining a conceptually distinct subset of the entire Pipeline, for example: "Build", "Test", and "Deploy", which is used by many plugins to visualize or present Jenkins Pipeline status/progress.

### Step
A single task; fundamentally steps tell Jenkins what to do inside of a Pipeline or Project.

```
stage "plan"{
  steps{
    sh " xxx"
  }
}
```

### withCredentials
```
withCredentials([usernamePassword(credentialsId: 'amazon', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
  // available as an env variable, but will be masked if you try to print it out any which way
  // note: single quotes prevent Groovy interpolation; expansion is by Bourne Shell, which is what you want
  sh 'echo $PASSWORD'
  // also available as a Groovy variable
  echo USERNAME
  // or inside double quotes for string interpolation
  echo "username is $USERNAME"
}
```
### Cleanup
https://plugins.jenkins.io/ws-cleanup/
