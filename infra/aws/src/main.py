import sys
import boto3
from .....modules.iam import Role

if __name__ == '__main__':

    for path in sys.path:
        print(path)

    #role = Role()
    print('Role created!')
