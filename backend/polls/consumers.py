import json
from channels.generic.websocket import AsyncWebsocketConsumer

# WebSocket consumer para manejar votos en tiempo real
class VoteConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Importar los modelos dentro del método para evitar AppRegistryNotReady
        from .models import Poll, Choice, Vote

        self.poll_id = self.scope['url_route']['kwargs']['poll_id']
        self.room_group_name = f"poll_{self.poll_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        from .models import Poll, Choice, Vote

        poll = Poll.objects.get(id=self.poll_id)

        counts = {
            choice.choice_text: Vote.objects.filter(choice=choice).count()
            for choice in poll.choices.all()
        }

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_votes",
                "data": counts
            }
        )

    async def send_votes(self, event):
        await self.send(text_data=json.dumps(event["data"]))
