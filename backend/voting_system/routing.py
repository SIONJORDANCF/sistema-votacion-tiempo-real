from django.urls import path
from polls.consumers import VoteConsumer
#ruta del websocket para votos
websocket_urlpatterns = [
    path("ws/votes/<int:poll_id>/", VoteConsumer.as_asgi()),
]
