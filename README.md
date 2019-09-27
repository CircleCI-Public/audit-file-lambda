# audit-file-lambda
This AWS lambda listens for S3 events and takes some action


See https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html#with-s3-example-configure-event-source for AWS configuration of CloudWatch/Lambda



## Build Locally


### Package Dependencies
*not required* unless adding uncommon dependencies
```
virtualenv ~/lambda_venv
source ~/lambda_venv/bin/activate
pip install boto3
pip install json
cd $VIRTUAL_ENV/lib/python3.7/site-packages
zip -r /tmp/InspectAuditBatch.zip .
cd -
```


### Package function as zip

```

zip -g InspectAuditBatch.zip InspectAuditBatch.py 
```


## Create Lambda on AWS

```
aws lambda create-function --function-name InspectAuditBatch \
--zip-file fileb://InspectAuditBatch.zip --handler InspectAuditBatch.handler --runtime python3.7 \
--timeout 10 --memory-size 1024 \
--role arn:aws:iam::241099261431:role/lamba-s3-role-eddies
```

## Update Function


```
zip -g InspectAuditBatch.zip InspectAuditBatch.py 
aws lambda update-function-code --function-name InspectAuditBatch \
--zip-file fileb://InspectAuditBatch.zip 
```


## Testing post deploy

`aws lambda invoke --function-name InspectAuditBatch --invocation-type Event \
--payload file://test/resources/s3event.json outputfile.txt`

