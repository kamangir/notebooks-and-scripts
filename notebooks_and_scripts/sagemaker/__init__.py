from sagemaker import get_execution_role
from abcli import logging
import logging

logger = logging.getLogger(__name__)

# https://github.com/aws/sagemaker-python-sdk/issues/300#issuecomment-1431539831
role = "arn:aws:iam::120429650996:role/service-role/AmazonSageMaker-ExecutionRole-20231022T170206"

try:
    role = get_execution_role()
except:
    pass

logger.info(f"sagemaker role: {role}")
