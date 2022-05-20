from django.urls import re_path
from . import consumers
import video.consumers

websocket_urlpatterns = [
     re_path(r'ws/FP/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
     re_path(r'ws/FP/video/(?P<v_name>\w+)/$', video.consumers.VideoConsumer.as_asgi())
]