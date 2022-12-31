# kaggle-Classify-forest-types-sagemaker
This repo is a reimplementation of https://github.com/mulargui/kaggle-Classify-forest-types-MLOps but using AWS Sagemaker. Sagemaker has a strong support for Jupyter Notebooks with Sagemaker Studio. Instead of using Jupyter Notebooks I use code and automation for building artifacts. 

The model is built and trained using Sagemaker instances. We are deploying the model in prod as a Sagemaker serverless endpoint. Sagemaker makes difficult to reach out to the endpoint using curl, so I created a small test client too.

You just need git and docker to run this repo in your laptop. Using containers massively simplifies the environment. Everything starts from you laptop (or DVM if is your preference) but the hard work is done in Sagemaker. You also need to setup a role with a policy to allow Sagemaker to access S3. 

Directories:\
**/api** Contains all the code and artifacts to deploy and test the model in Sagemaker.\
/api/scripts contains scripts to deploy and test the model.\
/api/src contains the code to deploy the model in sagemaker.\
/api/test contains the code of a test client.\
**/model/** contains all the code and artifacts to create and train the model.\
/model/scripts contains scripts to create and train the model.\
/model/scripts/trainlocal.sh creates and trains the model locally using containers. Very useful to iterate in the model without incurring Sagemaker costs.The resulting model is saved in the model-registry folder.\
/model/scripts/trainsg.sh creates and trains the model in Sagemaker.\
/model/src contains the code (python) of the model. \
/model/src/model.py is a module that encapsulates the definition of the neural network and how to train it. We use keras for modeling.\
/model/src/data.py is a module that encapsulates data engineering and validation.\
/model/src/trainsg.py creates and runs the job in Sagemaker to build the model.\
**/data** contains the data used for training the model. It is a copy of the original train data. \
**/model-registry** is a place to store and retrieve the parameters of the model when using local mode. \
**/infra** is the place for all the infrastructure needed to have the model in Prod. At this time there is just a pipeline folder with a shell script to build and deploy the service. There are also scripts to setup and remove AWS resources.\
/infra/pipeline/awsparams.sh declares all the AWS secrets needed to access AWS. Use awsparams-template.sh to build it.

Here are some ideas to sophisticate this service
1. Use jenkins pipelines/aws code pipelines to build and release. Scripts are ok to experiment but jenkins is a more robust system with the support of a broad  community. I did some experimentation with jenkins (including running it on k8s) here https://github.com/mulargui/jenkins-pipeline
2. Add performance testing (benchmarking). Compare the performance of the model (accuracy and latency mainly) with previous models and halt the release if not improving performance.
