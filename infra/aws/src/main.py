import sys
import boto3
from ...aws.modules.iam import Role

if __name__ == '__main__':

    role = Role()
    print('Role created!')
