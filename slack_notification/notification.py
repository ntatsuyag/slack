from pathlib import Path
import requests
import json

def get_config_info() -> str:
    # configのpathを取得する
    DIR = Path(__file__).resolve().parent #親ディレクトリのパスを取得
    CONFIG_PATH = str(DIR / Path("config.json"))

    # config.jsonからtoken,channel名を取得する
    with open(CONFIG_PATH, mode="r",encoding="utf-8") as config:
        data = json.load(config)
    print(data)
    TOKEN = data["token"]
    CHANNEL = data["channel"] # チャンネル名
    return TOKEN, CHANNEL

def send_message(message:str,username='from_notification'):
    token,channel = get_config_info() #configから情報を取得
    api_url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": "Bearer " + token}
    data  = {
        'channel': channel,
        'text': message,
        'username': username
    }
    return requests.post(api_url, headers=headers, data=data) # 送信 and 値をreturn

def main():
    send_message(message="test")

if __name__ == "__main__":
    main()