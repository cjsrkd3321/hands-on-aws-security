import json
import logging
import os
import boto3

from libs.utils import send_message_to_slack
from libs import actors

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

        actor = actors[evt](CHANNEL, detail, region, SOURCE_IPS)
        # Policy to receive logs only if successful
        if not actor.is_succeeded():
            return

        # Return message after parsing
        msg = actor.parse()
        # Determining Vulnerability
        if actor.is_vulnerable():
            # Output whether succeeded after remediation (True, False, None -> If no remediation)
            is_remediated = actor.remediate()
            fields = msg["attachments"][0]["blocks"][-1]["fields"]
            fields.append({"type": "mrkdwn", "text": f"*조치여부*:\n{is_remediated}"})

        send_message_to_slack(HOOK_URL, msg)
    except Exception as e:
        logger.error(f"{detail['eventID']} {region} {source} {evt}: {e}")
        send_message_to_slack(HOOK_URL, f"{region} {detail['eventID']} {evt} {e}")
