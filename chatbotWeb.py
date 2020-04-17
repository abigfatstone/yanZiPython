# -*- coding: UTF-8 -*-
#作者：姜子牙
#创建时间：20200417
#最后修改：

import urllib.request
import time
import ssl
import json
import string

class ChatbotWeb:
    def chat(self,inUserSaid):
        try:
            target = r'http://api.qingyunke.com/api.php?key=free&appid=0&msg='

            tmp = target + inUserSaid[0]
            url = urllib.parse.quote(tmp, safe=string.printable)
            page = urllib.request.urlopen(url)

            html = page.read().decode("utf-8")
            #json转为dict,json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
            res = json.loads(html)
            return ['chatbot_done',res['content'],'0']
        except:
            return ['chatbot_done','抱歉我没听明白','0'] 

# if __name__ == "__main__":
#     chatbotWeb = ChatbotWeb()
#     RES = chatbotWeb.chat("你好")
#     print(RES[1])

