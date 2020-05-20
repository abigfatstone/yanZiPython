
from channels.generic.websocket import AsyncWebsocketConsumer
import logging
import sys
import json

from .chatbotmanager import ChatbotManager

logger = logging.getLogger(__name__)

def formathtml(input_list):
    return_str = '<p>'
    for line_char in input_list:
        if line_char == '\n':
            return_str += '</p><p>'
        elif line_char == ' ':
            return_str += '&nbsp;'
        else:
            return_str += line_char
    return_str += '</p>'
    return return_str

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

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
                {'message': question, 'callback_key': 'list_function'})
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
            'message': message
        }))
