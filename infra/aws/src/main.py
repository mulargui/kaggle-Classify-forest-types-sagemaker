import sys
import boto3

if __name__ == '__main__':

    #check if the role for sagemaker exists
    rolelist = boto3.client('iam').list_roles(PathPrefix='/service-role/')['Roles']
    role = [r for r in rolelist if "AmazonSageMaker-ExecutionRole" in r['RoleName']][0]['Arn']

    if role:
        print(role)
        sys.exit(0)

    print ('no role')
