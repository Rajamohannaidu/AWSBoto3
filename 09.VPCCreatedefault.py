import boto3

# vpccilent=boto3.client("ec2")



# vpcId=""

# try:

#     response=vpccilent.create_default_vpc()

#     vpcId=response["Vpc"]["VpcId"]

#     print("Created Default VPC")

# except ClientError:

#     print("Not possible to create, Default VPC alreday exists")



# print( vpcId )


def fnCreateDefaultVPC(vpcClient):

    from botocore.exceptions import ClientError

    try:

        response=vpcClient.create_default_vpc()    

        vpcId=response["Vpc"]["VpcId"]

        print("Created Default VPC")

    except ClientError:

        print("Not possible to create, Default VPC alreday exists")


#Driver code

if __name__=="__main__":

    vpcclient=boto3.client("ec2")

    vpcId=fnCreateDefaultVPC(vpcclient)

    print(vpcId)