# AWS CLI

## check identity 
```
aws sts get-caller-identity
```
## check files on s3
```
aws s3 ls s3://ods
```
## copying local files to S3
```
aws s3 cp test.txt s3://mybucket/test2.txt
aws s3 cp . s3://packages-lambda-jin/ --recursive  --exclude "*" --include "*.zip"
https://docs.aws.amazon.com/cli/latest/reference/s3/
```
## copying a file from S3 to S3
```
aws s3 cp s3://mybucket/source.txt s3://mybucket/destination.txt
```
## copying an S3 object to a local file
```
aws s3 cp s3://mybucket/test.txt test2.txt
```

## copying an S3 object from one bucket to another
```
aws s3 cp s3://mybucket/test.txt s3://mybucket2/
```
## recursively copying local files to S3 (multiple files)
```
aws s3 cp myDir s3://mybucket/ --recursive --exclude "*.jpg"
```



