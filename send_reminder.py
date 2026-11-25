import requests

payload = {
    "content": "<@&1521486913620672542>",
    "allowed_mentions": {
        "parse": ["roles"]
    }
}

requests.post(WEBHOOK_URL, json=payload)
