import requests
import re
import random
from bs4 import BeautifulSoup

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('zPZKuzBxwID6lp6obwPGUFSrKSs2R73tzA03jUmz7ghx7KFOADc5w7qr7CpgyLtkJFS9qUNlGqElTtsjHKzUC3t2Ba6VLIcQAKkqhOOS2R8bgaTA38PHW3kc7WJxWu88RxyLq7fIIOoHAaD/8N75pgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('839c0486122c64e5d70fda36af44c7cf')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text", event.message.text)
    if event.message.text == "Hai":
        text_message = TextMessage(
            type=text
            text='Hai Juga Bro/Sist'
        )
        line_bot_api.reply_message(event.reply_token, text_message)


if __name__ == "__main__":
    app.run(debug = True, port = 80)
