import boto3

class AWSSageMaker:

    #sagemaker endpoint
    endpointname='predict-forest-type'

    #remnove sagemaker resources
    def remove(self):
        client = boto3.client('sagemaker')

        try:
            response = client.describe_endpoint_config(EndpointConfigName=self.endpointname)

            client.delete_endpoint(EndpointName=self.endpointname)
            client.delete_endpoint_config(EndpointConfigName=self.endpointname)

            client.delete_model(ModelName=response['ProductionVariants'][0]['ModelName'])
        except ClientError as error:
            print('No sagemaker resources...')

        return 1
 