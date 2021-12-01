#01.Import Packages
import json
import boto3
#02. Create Client
objClient=boto3.client('sts')
#03. Request Features/Options
response=objClient.get_caller_identity()
#04. Extract Details
userId=response["UserId"]
account=response['Account']
arn=response['Arn']


#05.Display Data
output={
"UserId":userId ,
"Account":account,
"Arn":arn
}



print(json.dumps(output,indent=4))