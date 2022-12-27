import sys
import boto3

#remove sagemaker role
rolename="AmazonSageMaker-ExecutionRole"
awsmanagedpolicy = 'arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'
    
client=boto3.client('iam')
client.detach_role_policy(
    RoleName=rolename,
    PolicyArn=awsmanagedpolicy
)client.delete_role(RoleName=rolename)

#remnove S3 bucket
bucket_name = "sagemaker-us-east-1-867679111813"
 
# First we list all files in bucket
client=boto3.client('s3')
response = client.list_objects_v2(Bucket=bucket_name, Prefix="/")
files_in_folder = response["Contents"]
files_to_delete = []
# We will create Key array to pass to delete_objects function
for f in files_in_folder:
    files_to_delete.append({"Key": f["Key"]})
# This will delete all files in the bucket
response = client.delete_objects(
    Bucket=bucket_name, Delete={"Objects": files_to_delete}
)

#remove sagemaker endpoint
 
print('teared down all aws sagemaker related resources!')
