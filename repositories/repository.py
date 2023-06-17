import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

class Repository:

    def __init__(self, db):
        self.db = db
        cred = credentials.Certificate("./auth/firebase.sa.key.json")
        self.app = firebase_admin.initialize_app(cred)
    
    def get_discord_user_id(self, userId: str) -> int:
        # get discord user id from firebase db
        return int(os.getenv("TEMP_USER_ID")) # ! int conversion is very important here

    def get_name_and_email(self, userId: str) -> tuple:
        # get name and email from firebase db
        user = auth.get_user(userId)
        # return ("Deven Paramaj", "devenparamaj.is19@bmsce.ac.in")
        return (user.display_name, user.email)

    def get_webhooks(self, userId: str):
        # get webhooks from firebase db
        return [os.getenv("TEMP_WEBHOOK_URL")]
