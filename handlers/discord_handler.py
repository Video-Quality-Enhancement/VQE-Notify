from models import DiscordClient
import os
from threading import Thread
from consumers import enhanced_video_notify_consumer
from services import DiscordService

def discord_handler():
    queue = "discord_queue"
    routing_key = "#.discord.#"

    client = DiscordClient()
    service = DiscordService(client)

    @client.event
    async def on_ready():
        print(f'Logged on as {client.user}!')
        print("starting discord consumer")
        
        t = Thread(
            target=enhanced_video_notify_consumer, 
            args=(queue, routing_key, service), 
            daemon=True)
        t.start()
        
        print("consumer started")
    
    client.run(os.getenv("DISCORD_TOKEN"))