import sys
import boto3
from iam import AWSRole

if __name__ == '__main__':

    #we just need to create the role to have this app work
    role = AWSRole()
    if role.create():
        print('Role created!')
