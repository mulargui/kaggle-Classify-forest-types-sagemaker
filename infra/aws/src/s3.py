import boto3

class AWSS3:
    #remnove S3 bucket
    def remove(self):

        #find the sagemaker bucket
        client = boto3.client('s3')
        bucketlist = client.list_buckets()
        bucketname = [b['Name'] for b in bucketlist['Buckets'] if "sagemaker" in b['Name']]

        #delete all objects in the bucket and the bucket itself
        if bucketname:
            boto3.resource('s3').Bucket(bucketname[0]).objects.delete()
            boto3.resource('s3').Bucket(bucketname[0]).delete()

        return 1