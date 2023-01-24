import sys
import boto3
from modules.iam import Role

if __name__ == '__main__':

    role = Role()
    if role.create():
        print('Role created!')
