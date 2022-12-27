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
bucket_name = "sagemaker-us-east-1-867679111813"

#find the sagemaker bucket
client = boto3.client('s3')
bucketlist = client.list_buckets()
bucket = [b['Name'] for b in bucketlist['Buckets'] if "sagemaker" in b['Name']]
print (bucket)

#delete all objects in the bucket and the bucket
if bucket:
    client = boto3.resource('s3')   
    bucket = client.Bucket(bucket)
    bucket.objects.all().delete()
    bucket.delete()

#remove sagemaker endpoint
 
print('teared down all aws sagemaker related resources!')
