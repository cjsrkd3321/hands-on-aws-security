from libs import actors
from libs.utils import is_our_cidr, get_user_info

# https://docs.aws.amazon.com/ko_kr/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html
# https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html
class ConsoleLogin:
    def __init__(self, channel, detail, region, our_ips=[]):
        self.channel = channel
        self.detail = detail
        self.region = region
        self.our_ips = our_ips

    def is_succeeded(self):
        res = self.detail["responseElements"]
        if res.get("ConsoleLogin") != "Success":
            return False
        return True

    def parse(self):
        add_evt_data = self.detail["additionalEventData"]
        evt = self.detail["eventName"]
        src_ip = self.detail["sourceIPAddress"]
        u_type, arn, user_name, role_name = get_user_info(self.detail["userIdentity"])

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
                                "text": f"*{evt}* ({self.region})",
                            },
                        },
                        {
                            "type": "divider",
                        },
                        {
                            "type": "section",
                            "fields": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"*시간:*\n{self.detail['eventTime']}",
                                },
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
                                    "text": f"*종류:*\n{u_type}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*사용자:*\n{arn}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*이름:*\n{user_name or role_name}",
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*MFA:*\n{add_evt_data.get('MFAUsed')}",
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
        return None


if __name__ != "__main__":
    actors[ConsoleLogin.__name__] = ConsoleLogin
