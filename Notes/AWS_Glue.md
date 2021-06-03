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
- local debugging?


### import/install 3rd party packages
```
key: --additional-python-modules 
value: pendulum==2.1.2,s3fs==0.5.2
```
https://docs.aws.amazon.com/glue/latest/dg/reduced-start-times-spark-etl-jobs.html

### import parameteres
```
set up para in glue settings
key: dev value:123

# import para in python scripts
args = getResolvedOptions(sys.argv, ['dev'])
```

### Glue Dev endpoints and notebook
- official tutorial https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-tutorial-sage.html
- hands on video https://www.youtube.com/watch?v=zdaVBXfmSs0
