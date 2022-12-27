import sys
import boto3

#remove sagemaker role
rolename="AmazonSageMaker-ExecutionRole"
awsmanagedpolicy = 'arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
'''    
client=boto3.client('iam')
client.detach_role_policy(
    RoleName=rolename,
    PolicyArn=awsmanagedpolicy
)
client.delete_role(RoleName=rolename)
'''
#remnove S3 bucket
#find the sagemaker bucket
client = boto3.client('s3')
bucketlist = client.list_buckets()
bucketname = [b['Name'] for b in bucketlist['Buckets'] if "sagemaker" in b['Name']]

#delete all objects in the bucket and the bucket itself
if bucketname:
    boto3.resource('s3').Bucket(bucketname[0]).objects.delete()
    boto3.resource('s3').Bucket(bucketname[0]).delete()

#remove sagemaker endpoint
 
print('teared down all aws sagemaker related resources!')
