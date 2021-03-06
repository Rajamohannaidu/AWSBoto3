#01.Import Packages
import boto3
#02. Create Client
objClient=boto3.client('iam')
#03. Request Features/Options API=GetPaginator/ListRoles  boto3=get_paginator(list_roles)
objPaginator=objClient.get_paginator('list_roles')

#print(type(objPaginator))
#print(objPaginator)

for page in objPaginator.paginate():
    for r in page['Roles']:
        print(r["RoleName"])