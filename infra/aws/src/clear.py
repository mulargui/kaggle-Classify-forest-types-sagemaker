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

# Retrieve the list of existing buckets
client = boto3.client('s3')
bucketlist = client.list_buckets()
bucket = [b['Name'] for b in bucketlist['Buckets'] if "sagemaker" in b['Name']]

#delete all objects in the bucket
if bucket:
    response = client.list_objects_v2(Bucket=bucket, Prefix="/")
    files_in_folder = response["Contents"]
    files_to_delete = []
    # We will create Key array to pass to delete_objects function
    for f in files_in_folder:
        files_to_delete.append({"Key": f["Key"]})
    client.delete_objects(
        Bucket=bucket, Delete={"Objects": files_to_delete}
    )

#remove sagemaker endpoint
 
print('teared down all aws sagemaker related resources!')
