import sys
import boto3

if __name__ == '__main__':

    print(sys.path)
    #sys.path.append('/repo')
    from modules.iam import Role

    role = Role()
    if role.create():
        print('Role created!')

