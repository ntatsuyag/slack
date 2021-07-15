# 設定
slack_notificationの下にconfig.jsonを作成

例
```
{
    "token":"トークン情報",
    "channel":"チャンネル名"
}
```
# 機能
`get_config_info`: config.jsonからトークンとチャンネル名の情報を取得する \
`send_message`: メッセージを送信する

# 公式ドキュメント
https://api.slack.com/methods/chat.postMessage/test