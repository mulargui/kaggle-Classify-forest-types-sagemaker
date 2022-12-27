#install packages
pip install -q --upgrade pip
pip install -q --upgrade boto3

# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/infra\/aws\/scripts//g')

#install aws resources
python3 $REPOPATH/infra/aws/src/clear.py