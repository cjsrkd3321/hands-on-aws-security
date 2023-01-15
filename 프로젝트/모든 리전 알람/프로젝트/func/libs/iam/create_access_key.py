import boto3

from libs.utils import is_our_cidr


def detect_create_access_key(channel, detail, region, our_ips=[]):
    event_time = detail["eventTime"]
    arn = detail["userIdentity"]["arn"]
    access_key = detail["userIdentity"]["accessKeyId"]

    event_name = detail["eventName"]
    src_ip = detail["sourceIPAddress"]

    created_access_key_info = detail["responseElements"]["accessKey"]

    # Root 엑세스 키는 UserName이 존재하지 않음(계정별칭을 추가하면 생김)
    user_name = created_access_key_info.get("userName", "root")
    created_access_key_id = created_access_key_info["accessKeyId"]

    is_deleted = False
    if not is_our_cidr(src_ip, our_ips):
        iam = boto3.client("iam")
        try:
            iam.delete_access_key(UserName=user_name, AccessKeyId=created_access_key_id)
            is_deleted = True
        except iam.exceptions.NoSuchEntityException:
            pass

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
                            "text": f"*{event_name}* ({region})",
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
                                "text": f"*계정:*\n{detail['recipientAccountId']}",
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
                            {
                                "type": "mrkdwn",
                                "text": f"*삭제여부:*\n{is_deleted}",
                            },
                        ],
                    },
                ],
            }
        ],
    }
