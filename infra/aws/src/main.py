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

    policy={
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
