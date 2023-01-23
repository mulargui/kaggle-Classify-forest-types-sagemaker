import sys
import boto3
from ....modules import iam

if __name__ == '__main__':

    for path in sys.path:
        print(path)

    role = Role()
    print('Role created!')
