import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

os.environ['SLACK_BOT_TOKEN'] = 'xoxb-854421202215-3784939796468-d8QKNSIjuLaz7mMel9UEZQuA'
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def postMessage(text, channel = "#mlops"):
    try:
        response = client.chat_postMessage(channel=channel, text=text)
        assert response["message"]["text"] == text
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
    return True
