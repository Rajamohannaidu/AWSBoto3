#upload_file(file_name,bucket_name,object_name)   upload_fileobj()
import pathlib
import boto3

BASE_DIR=pathlib.Path(__file__).parent.resolve()
bucket_name="testmybucket202010"
bpath=BASE_DIR.__str__()

file_name=bpath+"\requirements.txt"

object_name=file_name

s3client=boto3.client("s3")

#s3client.upload_file(BASE_DIR+"\\"+file_name,bucket_name,object_name)

print("File Uploaded")
print(file_name)