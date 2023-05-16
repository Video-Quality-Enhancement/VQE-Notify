from dotenv import load_dotenv
import pika, sys, os
import asyncio
import discord
from threading import Thread

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(intents=intents, *args, **kwargs)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        t = Thread(target=consumer, args=(self,))
        t.daemon = True
        t.start()
        print("consumer started")

async def send_user_message(client: MyClient, user_id: int, message: str):
    user = client.get_user(user_id)
    if user is not None:
        await user.send(message)
        print(user.id, message)
    else:
        print("user not found", user_id)

def consumer(client: MyClient):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        asyncio.run_coroutine_threadsafe(send_user_message(client, 432200040891809793, body), client.loop)
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def main():
    load_dotenv()
    client = MyClient()
    client.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)