import json
import boto3

#01.Select IAM Role
iam=boto3.client("iam")
role=iam.get_role("RolenName=r103decmujahed")
print("----------------")

#02.Create Lambda .Zip file
dir_name=r"C:\Practicals\02.svodaaws\serverlesssarchi"
output_file="lambda"
import shutil
shutil.make_archive(output_file,'zip',dir_name)
print("Zip Created  Kindly check ...")