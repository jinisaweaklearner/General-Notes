# AWS CLI

### check identity 
aws sts get-caller-identity

### check files on s3
aws s3 ls s3://ods

#### Copying a local file to S3
aws s3 cp test.txt s3://mybucket/test2.txt

### Copying a file from S3 to S3
aws s3 cp s3://mybucket/source.txt s3://mybucket/destination.txt

### Copying an S3 object to a local file
aws s3 cp s3://mybucket/test.txt test2.txt

### Copying an S3 object from one bucket to another
aws s3 cp s3://mybucket/test.txt s3://mybucket2/

### Recursively copying local files to S3 (multiple files)
aws s3 cp myDir s3://mybucket/ --recursive --exclude "*.jpg"




