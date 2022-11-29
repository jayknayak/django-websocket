import json

from channels.generic.websocket import AsyncWebsocketConsumer


class WebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('connected')
        await self.channel_layer.group_add(
            'message',
            self.channel_name
        )

        await self.accept()

        # To close the connection after timeout

        # await asyncio.sleep(5)
        # await self.close()

    async def welcome_msg(self, event):
        # Send message to WebSocket
        print('inside welcome_msg')
        await self.send(text_data=json.dumps({
            'type': event['type'],
            'message': 'Welcome to Websocket'
        }))

    async def disconnect(self, close_code):
        print('disconnected')
        await self.channel_layer.group_discard(
            'message',
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        receive_type = text_data_json['type']
        # message = text_data_json['message']
        package = {
            'type': receive_type,
        }

        await self.channel_layer.group_send(
            'message',
            package
        )
