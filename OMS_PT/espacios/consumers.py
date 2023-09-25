import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificacionOrdenConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'order_notification_group'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def notify_order_created(self, event):
        await self.send(text_data=json.dumps({
            'message': 'Nueva orden creada',
        }))