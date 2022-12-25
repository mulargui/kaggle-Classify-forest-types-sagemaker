# Absolute path to this file
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/model\/scripts//g')

#install aws resources
python3 $REPOPATH/infra/aws/src/main.py