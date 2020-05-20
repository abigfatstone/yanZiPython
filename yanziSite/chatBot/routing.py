# from . import consumer

# channel_routing = {
#     # TODO: From the original examples, there is more (https://github.com/jacobian/channels-example/)
#     'websocket.connect': consumer.ws_connect,
#     'websocket.receive': consumer.ws_receive,
#     'websocket.disconnect': consumer.ws_disconnect,
# }

from django.urls import re_path

# from . import consumer
from . import botConsumers

websocket_urlpatterns = [
    re_path(r'ws/chatbot/(?P<room_name>\w+)/$', botConsumers.ChatConsumer),
]