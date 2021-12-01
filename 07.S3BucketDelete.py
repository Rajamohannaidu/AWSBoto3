import boto3

#client -->delete_bucket() , resource --> bucket.delete()
#s3client=boto3.client("s3")
#s3client.delete_bucket("rajamohannaiduboto3")
#print("Bucket Deleted")

#s3resource=boto3.resource("s3")
#bucketName=input("Enter the Bucket Name to Delete:")
#Bucket=s3resource.Bucket(bucketName)
#Bucket.delete()
#print("Bucket Deleted")

s3resource=boto3.resource("s3")
bucketName="rajamohannaiduboto3"
Bucket=s3resource.Bucket(bucketName)

def cleanup_bucket_objects(myBucket):
    #Delete all Objects

    for obj in myBucket.objects.all():
        obj.delete()
    #if object has version delete version with objects
    
    for objver in myBucket.object_versions.all():
        objver.delete()

#Delete all objects from Bucket
cleanup_bucket_objects(Bucket)

#Delete an empty Bucket
Bucket.delete()