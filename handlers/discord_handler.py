from models import DiscordClient
import os
from threading import Thread
from consumers import notification_consumer
from services import DiscordService

def discord_handler():
    queue = "discord_queue"
    routing_key = "#.discord.#"

    client = DiscordClient()
    service = DiscordService(client)

    @client.event
    async def on_ready():
        print(f'Logged on as {client.user}!')
        
        t = Thread(target=notification_consumer, args=(queue, routing_key, service.send_discord_notification))
        t.daemon = True
        t.start()
        
        print("consumer started")
    
    client.run(os.getenv("DISCORD_TOKEN"))