import translate as ts

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)

line_bot_api = LineBotApi('e+lYBSQ03lFlvBC5DT5vi/xEDYgCpGi5mh7btYPEfGWbI4QQuld0CWDuzRfYnbjaVC6kAunXgj2VjtIa4q8jPABWRIimQQ2dC4SaOSObgzkoPpNc4dg4WKjD6244dcOthOL1ZThMuiLyw563BBj/4gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('741ebc851f8f132a6ff51c47d5931d64')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text)
    a = ts.swapp(msg)
    if(a != "-1"):
        message = TextSendMessage(text=a)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
