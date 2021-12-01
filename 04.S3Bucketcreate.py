import boto3
import os

s3=boto3.client("s3")

AWS_REGION=os.environ["RC"]

print("you passed region as ",AWS_REGION)

bucketName="rajamohannaiduboto3"
location={'LocationConstraint':AWS_REGION}

response=s3.create_bucket(Bucket=bucketName,CreateBucketConfiguration=location)
print("check wit : aws s3 ls")