import boto3

class Role:
    #name of the role to create
    rolename="AmazonSageMaker-ExecutionRole"

    #aws managed policy
    awsmanagedpolicy = 'arn:aws:iam::aws:policy/AmazonSageMakerFullAccess'

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

    #create sagemaker role
    def create(self):

        #check if the role for sagemaker exists
        client=boto3.client('iam')
        rolelist = client.list_roles(PathPrefix='/')['Roles']
        role = [r for r in rolelist if self.rolename in r['RoleName']]

        if role:
            print('role exists')
            print(role)
            return 1

        #otherwise create the role
        try:
            role = client.create_role(
                RoleName=self.rolename,
                AssumeRolePolicyDocument=self.trustpolicy,
                Description='This role allows Sagemaker access to other AWS resources on behalf of this account, ie S3'
            )
        except ClientError as error:
            print('Unexpected error occurred... Role could not be created:', error)
            return 0        

        #attach aws managed policy
        try:
            client.attach_role_policy(
                RoleName=self.rolename,
                PolicyArn=self.awsmanagedpolicy
            )
        except ClientError as error:
            print('Unexpected error occurred... hence cleaning up')
            client.delete_role(RoleName=self.rolename)
            print('Role could not be created:', error)
            return 0
        
        return 1

    #remove sagemaker role
    def remove(self):

        client=boto3.client('iam')
        client.detach_role_policy(
            RoleName=self.rolename,
            PolicyArn=self.awsmanagedpolicy
        )
        client.delete_role(RoleName=self.rolename)

        return 1