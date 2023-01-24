import sys
import boto3

if __name__ == '__main__':

    for path in sys.path:
        print(path)

    from ....modules import iam

    role = iam.Role()
    print('Role created!')
