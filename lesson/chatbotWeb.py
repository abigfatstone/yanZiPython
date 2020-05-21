# -*- coding: UTF-8 -*-
# 作者：姜子牙
# 创建时间：2020-04-17
# 最后修改：

import urllib.request
import time
import ssl
import json
import string
import requests


class ChatbotWeb:
    # def __init__(self):
    #     with open("resource/xiaobing.conf", "r") as f:  # 打开文件
    #         data = f.readlines()  # 读取文件
    #         self.uid = data[0].split('=')[1].strip()
    #         self.source = data[1].split('=')[1].strip()
    #         self.SUB = data[2].split('=')[1].strip()
    #         self.isDebug = 0
    #         if self.isDebug == 1:
    #             print(self.uid,self.source,self.SUB)

    def qingyunke(self, inUserSaid):
        target = r'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
        tmp = target + inUserSaid
        url = urllib.parse.quote(tmp, safe=string.printable)
        page = urllib.request.urlopen(url)

        html = page.read().decode("utf-8")
        # json转为dict,json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
        res = json.loads(html)
        return res['content']

    def xiaobing(self, msg):

        url_send = 'https://api.weibo.com/webim/2/direct_messages/new.json'
        data = {
            'text': msg,
            'uid': self.uid,
            'source': self.source
        }
        headers = {
            'cookie': 'SUB='+self.SUB,
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Referer': 'https://api.weibo.com/chat/'
        }
        response = requests.post(url_send, data=data, headers=headers).json()
        sendMsg = response['text']

        # time.sleep(1)

        while True:
            url_get = 'https://api.weibo.com/webim/2/direct_messages/conversation.json?uid={}&source={}'.format(
                self.uid, self.source)
            response = requests.get(url_get, headers=headers).json()
            getMsg = response['direct_messages'][0]['text']
            if sendMsg == getMsg:
                time.sleep(1)
            else:
                return getMsg

    def chatWithBot(self, inUserSaid):

        try:
            # res = self.xiaobing(inUserSaid)
            res = self.qingyunke(inUserSaid['message'])
            return {'message': res, 'callback_key': 'list_function', 'step_id': 0}
        except:
            return {'message': '输入list试试看吧', 'callback_key': 'list_function', 'step_id': 0}


if __name__ == "__main__":
    chatbotWeb = ChatbotWeb()
#     RES = chatbotWeb.chat("你好")
#     print(RES[1])

    msg = {'message': '你的速度好慢'}
    print("me>>", msg)
    res = chatbotWeb.chatWithBot(msg)
    print("AI>>", res)
