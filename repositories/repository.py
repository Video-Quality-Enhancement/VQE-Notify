import os

class Repository:

    def __init__(self, db):
        self.db = db
    
    def get_discord_user_id(self, userId: str) -> int:
        # get discord user id from firebase db
        return int(os.getenv("TEMP_USER_ID")) # ! int conversion is very important here

    def get_name_and_email(self, userId: str) -> tuple:
        # get name and email from firebase db
        return ("Deven Paramaj", "devenparamaj.is19@bmsce.ac.in")

    def get_webhooks(self, userId: str):
        # get webhooks from firebase db
        return [os.getenv("TEMP_WEBHOOK_URL")]