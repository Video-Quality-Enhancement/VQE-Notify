import asyncio
from models import DiscordClient, EnhancedVideoNotifyRequest
from .abstracts import EnhancedVideoNotify
from repositories import Repository


class DiscordService(EnhancedVideoNotify):

    def __init__(self, client: DiscordClient):
        self.client = client
        self.repository = Repository(None)

    async def send_user_message(self, discord_user_id: int, notify_request: EnhancedVideoNotifyRequest):
        user = self.client.get_user(discord_user_id)
        if user is not None:
            await user.send(notify_request.enhancedVideoUrl)
            print("discord message sent to user", user) # TODO: log stuff here
        else:
            print("user not found", discord_user_id) 
        
    def notify(self, notify_request: EnhancedVideoNotifyRequest):
        discord_user_id = self.repository.get_discord_user_id(notify_request.userId)
        asyncio.run_coroutine_threadsafe(self.send_user_message(discord_user_id, notify_request), self.client.loop)
        # print("sent to discord") # TODO: log stuff here
