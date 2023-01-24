import sys
import boto3

if __name__ == '__main__':

    #sys.path.insert(1, '/repo')
    sys.path.append('/repo')
    from modules.iam import Role

    role = Role()
    if role.create():
        print('Role created!')

