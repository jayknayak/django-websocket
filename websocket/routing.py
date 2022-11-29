from django.conf.urls import url

from websocket import consumers

websocket_urlpatterns = [
    url(r'^ws/message/$', consumers.WebsocketConsumer),
]
