import sys
import boto3
from infra.aws.pckgs.iam import AWSRole
from infra.aws.pckgs.s3 import AWSS3
from infra.aws.pckgs.sagemaker import AWSSageMaker

if __name__ == '__main__':

    #remove sagemaker role
    role = AWSRole()
    if role.remove():
        print('Role removed!')

    #remnove S3 bucket
    bucket = AWSS3()
    if bucket.remove():
        print('bucket removed!')

    #remnove sagemaker resources
    sg = AWSSageMaker()
    if sg.remove():
        print('sagemaker removed!')
                            
    print('teared down all AWS related resources!')
