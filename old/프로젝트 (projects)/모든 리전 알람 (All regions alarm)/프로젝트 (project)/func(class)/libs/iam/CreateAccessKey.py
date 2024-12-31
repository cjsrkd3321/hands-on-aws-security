import boto3

from libs import actors
from libs.utils import is_our_cidr


class CreateAccessKey:
    def __init__(self, channel, detail, region, our_ips=[]):
        self.channel = channel
        self.detail = detail
        self.region = region
        self.our_ips = our_ips

    def is_succeeded(self):
        if not self.detail["responseElements"]:
            return False
        return True

    def parse(self):
        event_time = self.detail["eventTime"]
        arn = self.detail["userIdentity"]["arn"]
        access_key = self.detail["userIdentity"]["accessKeyId"]
        event_name = self.detail["eventName"]
        src_ip = self.detail["sourceIPAddress"]

        created_access_key_info = self.detail["responseElements"]["accessKey"]
        user_name = created_access_key_info.get("userName", "root")
        created_access_key_id = created_access_key_info["accessKeyId"]

        return {
            "channel": self.channel,
            "attachments": [
                {
                    "color": "#30db3f"
                    if is_our_cidr(src_ip, self.our_ips)
                    else "#eb4034",
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*{event_name}* ({self.region})",
                            },
                        },
                        {
                            "type": "section",
                            "fields": [
                                {"type": "mrkdwn", "text": f"*시간:*\n{event_time}"},
                                {
                                    "type": "mrkdwn",
                                    "text": f"*IP:*\n{src_ip}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*계정:*\n{self.detail['recipientAccountId']}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*발급인:*\n{arn}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*발급인키:*\n`{access_key}`",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*사용자:*\n{user_name}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*Access Key ID:*\n{created_access_key_id}",
                                },
                            ],
                        },
                    ],
                }
            ],
        }

    def is_vulnerable(self):
        src_ip = self.detail["sourceIPAddress"]
        if is_our_cidr(src_ip, self.our_ips):
            return False
        return True

    def remediate(self):
        created_access_key_info = self.detail["responseElements"]["accessKey"]
        user_name = created_access_key_info.get("userName", "root")
        created_access_key_id = created_access_key_info["accessKeyId"]

        is_deleted = False
        iam = boto3.client("iam")
        try:
            iam.delete_access_key(UserName=user_name, AccessKeyId=created_access_key_id)
            is_deleted = True
        except iam.exceptions.NoSuchEntityException:
            pass
        return is_deleted


if __name__ != "__main__":
    actors[CreateAccessKey.__name__] = CreateAccessKey
