# Terraform

### common commands
```
# initialize a working directory containing Terraform configuration files.
# about partial Configuration:
# https://www.terraform.io/docs/language/settings/backends/configuration.html#partial-configuration
terraform init -backend-config="bucket=s3_bucket_name"

# The persistent data stored in the backend belongs to a workspace (for dev, uat and prod)
terraform workspace select workspace || terraform workspace new workspace

# validate the code
terraform validate

# list all resources
terraform state list

# Proposing a set of change actions that should, if applied, make the remote objects match the configuration.
# -out=FILE to save a plan
# Sets values for potentially many input variables declared in the root module of the configuration
terraform plan -out=tfplan -var-file=./FILENAME.tfvars

terraform apply tfplan --auto-approve
```

### reformat the code
```
# formatting all the files
terraform fmt -recursive
```


### How we use resources across multiple repo?
- we use outputs from source repo as following
```
# global level
output = "role_data_engineer_arn" {
  value = module.iam.role_data_engineer_arn
}

# local level
output = "role_data_engineer_arn" {
  value = aws_iam_role.data_engineer.arn
}

```

- In target repo, we call it by using "data" via .tfstate 
```
# import remote state 
data "terraform_remote_state" "foundation" {
  backend = "s3"
  
  config = {
    bucket         = "terraform-state"
    key            = "filename.tfstate"
    region         = "ap-southeast-2"
  }
}

# use it when creating other resources
role = data.terraform_remote_state.foundation.outputs.role_data_engineer_arn

```

variables, locals and outputs https://www.terraform.io/docs/language/values/index.html

### s3 Backend
- store configuration locally and remotely https://www.terraform.io/docs/language/settings/backends/s3.html
- use data from remote state
```
terraform {
  backend "s3" {
    bucket         = "terraform-state"
    key            = "filename.tfstate"
    region         = "ap-southeast-2"
  }
}
```

### Common errors
- have the duplicated resource names
- the gap between AWS API and Terraform
    - aws_dms_replication_task replication_task_settings always reports as needing modification https://github.com/hashicorp/terraform-provider-aws/issues/1513
    - extra connection attributes in DMS s3 endpoints need to be in order, otherwise it will report as needing modification
- can't modify it when it's running
- dependencies bewtween multiple resources
