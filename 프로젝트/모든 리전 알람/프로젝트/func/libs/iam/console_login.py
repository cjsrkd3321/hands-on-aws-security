from libs.utils import is_our_cidr, get_user_info

# https://docs.aws.amazon.com/ko_kr/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html
# https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html
def detect_console_login(channel, detail, region, our_ips=[]):
    res = detail["responseElements"]
    if res.get("ConsoleLogin") != "Success":
        return

    add_evt_data = detail["additionalEventData"]
    evt = detail["eventName"]
    src_ip = detail["sourceIPAddress"]
    u_type, arn, user_name, role_name = get_user_info(detail["userIdentity"])

    return {
        "channel": channel,
        "attachments": [
            {
                "color": "#30db3f" if is_our_cidr(src_ip, our_ips) else "#eb4034",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*{evt}* ({region})",
                        },
                    },
                    {
                        "type": "divider",
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": f"*시간:*\n{detail['eventTime']}"},
                            {
                                "type": "mrkdwn",
                                "text": f"*IP:*\n{src_ip}",
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*계정:*\n{detail['recipientAccountId']}",
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
