import sys, os
import boto3

if __name__ == '__main__':

    for path in sys.path:
        print(path)

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    for path in sys.path:
        print(path)

    from ....modules.iam import Role

    role = Role()
    print('Role created!')
