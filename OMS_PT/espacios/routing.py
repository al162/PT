from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server', consumers.NotificacionOrdenConsumer.as_asgi())
]