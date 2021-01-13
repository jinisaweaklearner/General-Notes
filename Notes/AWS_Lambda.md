## location of packages in lambda layer
```
python/lib/python3.6/site-packages/{LibrariesGoHere}
sys.path.insert(1, '/opt')  # lambda version
```


Layer python tutorial 
https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d 

How to use packages in lambda layer
https://stackoverflow.com/questions/55695187/import-libraries-in-lambda-layers 

 

the size of unzip file should be under 250 MB 

The zip file for layers need to contain those folders: python/lib/python3.7/site-packages/{LibrariesGoHere}. 

The role need to have permission to get screts 

Setup timeout and memory 

Need to get the permission to AWS Aurura 


Make sure the lambda role can attach the policy AWSLambdaVPCAccessExecutionRole  

https://blog.shikisoft.com/running-aws-lambda-in-vpc-accessing-rds/ 



IAM role-based authentication to Amazon Aurora from serverless applications 

https://aws.amazon.com/blogs/database/iam-role-based-authentication-to-amazon-aurora-from-serverless-applications/ 

 

Using HTTP Methods for RESTful Services 

https://www.restapitutorial.com/lessons/httpmethods.html 

 

## SAM
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-validate.html 

Multiple lambda functions 

https://aws.amazon.com/blogs/compute/introducing-simplified-serverless-application-deplyoment-and-management/ 
 

Error: Failed to create changeset for the stack: sam_load_valuation, An error occurred (ValidationError) when calling the CreateChangeSet operation: 1 validation error detected: Value 'sam_load_valuation' at 'stackName' failed to satisfy constraint: Member must satisfy regular expression pattern: [a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/._+]* 

If we changed sth, need to build again 

Docs 

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html 



https://aws.amazon.com/blogs/aws/new-aws-toolkits-for-pycharm-intellij-preview-and-visual-studio-code-preview/ 

 