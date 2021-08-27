
before unload data from redshift to s3

- make sure Associated IAM roles is there
- IAM role has the trust entity "redshift"




```
    unload ('select * from public.date')
    to 's3://jin-test-123/test0827'
    IAM_ROLE 'arn:aws:iam::673765577618:role/redshift_to_s3_migration_role' 
    header
    manifest
    CSV DELIMITER AS '|'
    maxfilesize 5 mb;
```




