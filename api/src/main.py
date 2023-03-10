import sys
import boto3
import sagemaker
from sagemaker.tensorflow import TensorFlowModel
from sagemaker.serverless.serverless_inference_config import ServerlessInferenceConfig

if __name__ == '__main__':

    #role used in sagemaker
    #role = sagemaker.get_execution_role() #this only works on Sagemaker Studio
    rolelist = boto3.client('iam').list_roles(PathPrefix='/')['Roles']
    role = [r for r in rolelist if "AmazonSageMaker-ExecutionRole" in r['RoleName']][0]['Arn']

    #latest model built
    bucket = sagemaker.Session().default_bucket() 
    result = boto3.client('s3').list_objects_v2(Bucket=bucket, Prefix='', Delimiter='/')['CommonPrefixes']
    folderlist = [r['Prefix'] for r in result]
    lastmodel = sorted(folderlist, reverse=True)[0]
    model_url = 's3://' + bucket + '/' + lastmodel + 'output/model.tar.gz'

    #configuration
    serverless_config = ServerlessInferenceConfig(
        memory_size_in_mb=1024,
        max_concurrency=1
    )

    #endpoint creation
    model = TensorFlowModel(model_data=model_url, role=role, framework_version='2.1.0')
    model.deploy(serverless_inference_config=serverless_config, endpoint_name='predict-forest-type')
