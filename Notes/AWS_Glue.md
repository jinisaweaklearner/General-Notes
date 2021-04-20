# Glue

- steps of create GLUE IAM
https://docs.aws.amazon.com/glue/latest/dg/getting-started-access.html

- addtional policy for s3
https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html

- errors when using glue crawler
```
ERROR : Insufficient Lake Formation permission(s) on csc (Database name: csc) (Service: AWSGlue; Status Code: 400; Error Code: AccessDeniedException;

solution: grant access in lake formation
https://stackoverflow.com/questions/57581398/aws-glue-cannot-create-database-from-crawler-permission-denied
```

- can't define output names when you use glue package to store parquet files
- can use normal python script

- use 3rd party python packages
