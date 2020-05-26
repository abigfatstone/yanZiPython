from channels.generic.websocket import AsyncWebsocketConsumer
import logging
import sys
import json

from .chatbotmanager import ChatbotManager

logger = logging.getLogger(__name__)


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

        text_data_json['session_id'] = self.room_name
        try:
            answer = ChatbotManager.callBot(text_data_json)
        except:
            answer['message'] = 'error:internal error'
        print(text_data_json,'->',answer)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'answer': answer,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print(event)
        answer = event['answer']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': answer['message'],
            'type': answer['answer_type'],
            'session_id': self.room_name
        }))
