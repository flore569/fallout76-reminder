import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

ROLE_ID = "877576271201206272"

message = f"""<@&{ROLE_ID}>

今日は水曜日です。
本日20:00から Fallout 76 を開始します。

予定がある場合は早めにご連絡ください。
"""

requests.post(
    WEBHOOK_URL,
    json={
        "content": message,
        "allowed_mentions": {
            "parse": ["roles"]
        }
    }
)
