import sys
import boto3

if __name__ == '__main__':

    #check if the role for sagemaker exists
    client=boto3.client('iam')
    rolelist = client.list_roles(PathPrefix='/service-role/')['Roles']
    role = [r for r in rolelist if "AmazonSageMaker-ExecutionRole" in r['RoleName']][0]['Arn']

    if role:
        sys.exit(0)

    #create the role
    trustpolicy='''{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "sagemaker.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'''

    try:
        role = client.create_role(
            RoleName='AmazonSageMaker-ExecutionRole-test',
            AssumeRolePolicyDocument=trustpolicy,
            Description='This role allows Sagemaker access to other AWS resources on behalf of this account, ie S3'
        )
    except ClientError as error:
        print('Unexpected error occurred... Role could not be created:', error)
        sys.exit(-1)        

    #attach aws managed policy
    awsmanagedpolicy = 'arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'

    try:
        client.attach_role_policy(
            RoleName='AmazonSageMaker-ExecutionRole-test',
            PolicyArn=awsmanagedpolicy
        )
    except ClientError as error:
        print('Unexpected error occurred... hence cleaning up')
        client.delete_role(
            RoleName='AmazonSageMaker-ExecutionRole-test'
        )
        print('Role could not be created:', error)
        sys.exit(-1)

    policy='''{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:DeleteObject",
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::*"
                ]
            }
        ]
    }

    try:
        policy_res = client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy
        )
        policy_arn = policy_res['Policy']['Arn']
    except ClientError as error:
        if error.response['Error']['Code'] == 'EntityAlreadyExists':
            print('Policy already exists... hence using the same policy')
            policy_arn = 'arn:aws:iam::' + account_id + ':policy/' + policy_name
        else:
            print('Unexpected error occurred... hence cleaning up', error)
            iam_client.delete_role(
                RoleName= role_name
            )
            return 'Role could not be created...', error
    '''
