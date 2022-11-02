#======LINE需求套件=====
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#======LINE需求套件=====

#======呼叫檔案內容=====
from model import *
#from new import *

#======呼叫檔案內容=====

#======python的函數庫==========
from googletrans import Translator 
import os
import time
import openai 
import threading 
import requests

#======python的函數庫==========

#======讓heroku不會睡著======
'''def wake_up_heroku():
    while 1==1:
        url = 'https://carebot0.herokuapp.com/' + 'heroku_wake_up'
        res = requests.get(url)
        if res.status_code==200:
            print('喚醒heroku成功')
        else:
            print('喚醒失敗')
        time.sleep(28*60)

threading.Thread(target=wake_up_heroku).start()'''
#======讓heroku不會睡著======

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('cg2xg/YSwQJczR1rlcGXvfmViywSkfsEJZsUCFu0DnxmeLDKXR4n81GnBt7hvsinSWdoEfBcD5HcetDV1+KZi6d78pPXrTAfiWHZrz5qeTb20fH4Eg3/rwSvvMRRSbHEHlwKYSbdRgGjQHkmDPAOEwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b6b443016624945c1ad4509931b65e2a')

# 監聽所有來自 /callback 的 Post Request
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

def translate_text(text,de):
    translator = Translator()
    result = translator.translate(text, dest=de).text
    return result

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    msg = translate_text(event.message.text, 'en')#輸入的句子轉英文
    ans=ask(msg)#輸出英文
    ans = translate_text(ans, 'en')#輸出轉成中文``
    message = TextSendMessage(text=ans)
    line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)

@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
