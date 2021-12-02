import boto3

def fnCreateCustomVPC(vpcResource,IpCidr):

    from botocore.exceptions import ClientError

    vpcId="Not Set"

    try:

        response=vpcResource.create_vpc(CidrBlock=IpCidr,
        InstanceTenancy="default",
        TagSpecifications=[{"ResourceType":"vpc", "Tags":[{'Key':'Name','Value':'rajamohanvpc'}]}])    

        vpcId=response.id

        print("Created custom VPC")

    except ClientError as ce:

        print("Not possible to create",ce)
        return vpcId


#Driver code

if __name__=="__main__":

    vpcresource=boto3.resource("ec2",region_name="ap-south-1")
    Ip_Cidr="192.168.0.0/26"

    vpcId=fnCreateCustomVPC(vpcresource,Ip_Cidr)

    print(vpcId)