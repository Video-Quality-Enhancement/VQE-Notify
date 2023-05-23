from dotenv import load_dotenv
from handlers import discord_handler

def main():
    load_dotenv()
    discord_handler()
