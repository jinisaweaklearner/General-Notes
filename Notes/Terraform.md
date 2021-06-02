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
terraform fmt -recursive
```

### variables, locals and outputs
https://www.terraform.io/docs/language/values/index.html


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
# import xxx 
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



