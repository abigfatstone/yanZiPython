from channels.generic.websocket import AsyncWebsocketConsumer
import logging
import sys
import json

from .chatbotmanager import ChatbotManager
logger = logging.getLogger(__name__)


def formathtml(input_list):
    nLine = 0
    return_str = ''
    line_list = input_list.split(':')
    if line_list[0] == '文件地址':
        file_name = line_list[1].split('/')[-1]
        file_url = 'http://yanzi.cloudoc.cn:8000/static/'
        return_str = "<a href=\"" + file_url + file_name + "\">点击查看文件</a>"
    else:
        for line_char in input_list:
            if line_char == '\n':
                nLine += 1
                if nLine == 1:
                    return_str += '<p>'
                else:
                    return_str += '</p><p>'
            elif line_char == ' ':
                return_str += '&nbsp;'
            else:
                return_str += line_char
        return_str += '</p>'
    return return_str


class ChatConsumer(AsyncWebsocketConsumer):

    # def __init__(self):
    #     # Model/dataset parameters
    #     self.SESSION_ID = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.SESSION_ID = self.room_name
        print(self.SESSION_ID)

        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        question = text_data_json['message']
        answer = ''
        try:
            aiReturn = ChatbotManager.callBot(
                {'message': question, 'callback_key': 'list_function', 'session_id': self.room_name})
            print(aiReturn)
            answer = formathtml(aiReturn['message'])
        except:  # Catching all possible mistakes
            logger.error("Unexpected error:")
            answer = 'Error: Internal problem'

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': answer
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message, 'type': 'text','session_id':self.room_name
        }))
