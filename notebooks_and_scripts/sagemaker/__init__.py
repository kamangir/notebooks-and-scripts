from sagemaker import get_execution_role
from notebooks_and_scripts.logger import logger

# https://github.com/aws/sagemaker-python-sdk/issues/300#issuecomment-1431539831
role = "arn:aws:iam::120429650996:role/service-role/AmazonSageMaker-ExecutionRole-20231022T170206"

try:
    role = get_execution_role()
except:
    pass

logger.info(f"sagemaker role: {role}")
