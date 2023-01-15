import json
import logging

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def send_message_to_slack(hook_url, slack_message, logger=logging.getLogger()):
    req = Request(hook_url, json.dumps(slack_message).encode("utf-8"))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message["channel"])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)


def is_our_cidr(src_ip, our_ips):
    if src_ip in our_ips:
        return True
    return False


# https://docs.aws.amazon.com/ko_kr/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html
# IAMUser, AssumedRole, FederatedUser, Root, AWSAccount, AWSService, Unknown, Directory
def get_user_info(user_identity):
    user_type = (ui := user_identity)["type"]
    role_name = ""
    if user_type in ["AssumedRole", "FederatedUser", "Role"]:
        if "sessionContext" in ui:
            # AWS SSO etc...
            # arn:aws:iam::ACCOUNT_ID:role/rextest
            arn = ui["sessionContext"]["sessionIssuer"]["arn"]
            role_name = arn.split("/")[-1]
        else:
            # External SAML etc...
            # "arn:aws:sts::ACCOUNT_ID:assumed-role/rextest/admin"
            arn = ui["arn"]
            role_name = arn.split("/")[-2]
        user_name = ui["principalId"].split(":")[-1]
    elif user_type in ["Root", "IAMUser"]:
        arn = ui["arn"]
        user_name = ui.get("userName", "root")
    elif user_type == ["Directory", "AWSAccount", "AWSService", "Unknown"]:
        arn = "NEED_CHECK"
        user_name = "NEED_CHECK"

    return user_type, arn, user_name, role_name
