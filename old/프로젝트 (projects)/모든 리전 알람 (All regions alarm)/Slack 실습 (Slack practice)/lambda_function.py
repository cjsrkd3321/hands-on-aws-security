import json
import logging

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

HOOK_URL = (
    "https://hooks.slack.com/services/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"
)
SLACK_CHANNEL = "#security-alarm"

if __name__ == "__main__":
    CONDITION = False
    # slack_message = {"channel": SLACK_CHANNEL, "text": f"*test*\ntest2"}
    slack_message = {
        "channel": SLACK_CHANNEL,
        "attachments": [
            {
                "color": "#30db3f" if CONDITION else "#eb4034",
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "EVENTNAME",
                        },
                    },
                    {
                        "type": "divider",
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": "*시간:*\nEVENTTIME"},
                            {
                                "type": "mrkdwn",
                                "text": "*IP:*\nIP",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*계정:*\nACCOUNT",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*종류:*\nUSER_TYPE",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*사용자:*\nARN",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*이름:*\nUSER_NAME",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*MFA:*\nMFA",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*SWITCH_FROM:*\nSWITCH_FROM",
                            },
                        ],
                    },
                ],
            }
        ],
    }

    req = Request(HOOK_URL, json.dumps(slack_message).encode("utf-8"))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message["channel"])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
