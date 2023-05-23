import os

class Repository:

    def __init__(self, db):
        self.db = db
    
    def get_discord_user_id(self, userId: str):
        # get discord user id from firebase db
        return os.getenv("TEMP_USER_ID")