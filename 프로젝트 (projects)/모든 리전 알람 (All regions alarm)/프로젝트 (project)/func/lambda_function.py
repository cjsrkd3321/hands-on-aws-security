import json
import logging
import os
import boto3

from libs.iam.console_login import detect_console_login
from libs.iam.create_access_key import detect_create_access_key
from libs.utils import send_message_to_slack

secrets = json.loads(
    boto3.client("secretsmanager").get_secret_value(
        SecretId=os.getenv("SECRET_ARN", "")
    )["SecretString"]
)

HOOK_URL = secrets.get("slack_webhook_url", "")
CHANNEL = secrets.get("slack_channel", "")
# https://docs.python.org/ko/3/howto/ipaddress.html#networks-as-lists-of-addresses
SOURCE_IPS = json.loads(os.getenv("SOURCE_IPS", "[]"))

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, _):
    msg = "EXCEPTION"
    try:
        print(type(event), event)
        source, detail = event["source"], event["detail"]

        evt = detail["eventName"]
        region = detail["awsRegion"]

        if evt == "ConsoleLogin":
            msg = detect_console_login(CHANNEL, detail, region, SOURCE_IPS)
        elif evt == "CreateAccessKey":
            msg = detect_create_access_key(CHANNEL, detail, region, SOURCE_IPS)
        else:
            return

        send_message_to_slack(HOOK_URL, msg)
    except Exception as e:
        logger.error(f"{detail['eventID']} {region} {source} {evt}: {e}")
        send_message_to_slack(HOOK_URL, f"{region} {detail['eventID']} {evt} {e}")
