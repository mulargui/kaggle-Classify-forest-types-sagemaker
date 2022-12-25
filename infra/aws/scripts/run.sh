#!/usr/bin/env bash

#
# You need to add your AWS credentials before executing this script for SGLOCAL and SG modes
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ACCOUNT_ID
# AWS_DEFAULT_REGION, AWS_REGION
#

set +x
export DEBIAN_FRONTEND=noninteractive
# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/api\/scripts//g')

# what you can do
CLEAR=N
DEPLOY=N

# you can also set the flags using the command line
for var in "$@"
do
	if [ "CLEAR" == "$var" ]; then CLEAR=Y 
	fi
	if [ "DEPLOY" == "$var" ]; then DEPLOY=Y 
	fi
done

#deploy iam role needed for sagemaker
if [ "${DEPLOY}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/repo \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
		tensorflow/tensorflow /bin/bash /repo/infra/aws/scripts/deploy.sh
fi

#tear down aws resources
if [ "${CLEAR}" == "Y" ]; then
	docker run -ti -v $REPOPATH:/repo \
		-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
		-e AWS_REGION -e AWS_DEFAULT_REGION \
		tensorflow/tensorflow  /bin/bash /repo/infra/aws/scripts/clear.sh
fi
