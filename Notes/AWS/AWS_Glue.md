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

### Update values
```
df = df.withColumn("row_is_current_fl",
 when((df['row_start_dt'] != date) & (
 df['pk'].isin(delete_list) & (df["row_is_current_fl"] == "Y")),
 "N").otherwise(df["row_is_current_fl"]))
```

### isin() vs join
If there is a very long list, try not to use .isin() function.
Instead, we can use join function to select records we want as following.
```
# get the "list"
df_pk = df.where(col('row_is_current_fl') == "Y").groupBy(['pk']).count().where(col('count') > 1).select('pk')

# get unchange part
df_unchange = df.join(df_pk, on = ['pk'], how='left_anti')

# get the updated part
df = df.join(df_pk, on = ['pk'], how='right')
```

### what is _$folder$ suffix in S3?
The "_$folder$" files are placeholders. Apache Hadoop creates these files when you use the -mkdir command to create a folder in an S3 bucket. Hadoop
doesn't create the folder until you PUT the first object. If you delete the "_$folder$" files before you PUT at least one object, Hadoop can't create the folder.
This results in a "No such file or directory" error.
https://aws.amazon.com/premiumsupport/knowledge-center/emr-s3-empty-files/

### How to drop duplicates and keep "first" in pyspark?
In pyspark, keep first is not supported in the function as It is hard to identify which one is the first. So, we have to order and repartition the data frame first.
https://medium.com/swlh/computing-global-rank-of-a-row-in-a-dataframe-with-spark-sql-34f6cc650ae5

### Switch between pyspark data frame and pandas data frame
```
df_spark = spark.createDataFrame(df_pandas)
df_pandas = df_spark.toPandas()
```
