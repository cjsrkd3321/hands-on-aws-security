import boto3
import json
from botocore.config import Config

client = boto3.client("secretsmanager", config=Config(region_name="us-east-1"))

response = json.loads(client.get_secret_value(SecretId="test")["SecretString"])

from pprint import pprint

print(response["test1"])
