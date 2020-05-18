from . import consumer
from channels.routing import route

channel_routing = {
    # TODO: From the original examples, there is more (https://github.com/jacobian/channels-example/)
    'websocket.connect': consumer.ws_connect,
    'websocket.receive': consumer.ws_receive,
    'websocket.disconnect': consumer.ws_disconnect,
}

# from channels.routing import route
# channel_routing = [
#     route("http.request", "myapp.consumers.http_consumer"),
#     ]