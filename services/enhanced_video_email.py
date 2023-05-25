from .gapi import Gmail
from .abstracts.enhanced_video_notify import EnhancedVideoNotify
from repositories import Repository
from models import EnhancedVideoNotifyRequest


class EnhancedVideoEmail(EnhancedVideoNotify):

    def __init__(self):
        self.repository = Repository(None)

    def notify(self, notify_request: EnhancedVideoNotifyRequest):
        name, email = self.repository.get_name_and_email(notify_request.userId)

        gmail = Gmail()
        gmail.send(
            to_email=email,
            subject="Enhanced Video",
            body=f"Hi {name},\n\nHere is your enhanced video: {notify_request.enhancedVideoUrl}\n\nRegards,\nVQE.AI"
        )

        print("mail sent to", email) # TODO: log stuff here
    