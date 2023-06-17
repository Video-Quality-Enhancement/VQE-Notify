from .abstracts.enhanced_video_notify import EnhancedVideoNotify
from repositories import Repository
from models import EnhancedVideoNotifyRequest
from firebase_admin import messaging

class PushNotification(EnhancedVideoNotify):

    def __init__(self):
        self.repository = Repository(None)

    def notify(self, notify_request: EnhancedVideoNotifyRequest):

        if notify_request.fcmTokens is None:
            return

        if len(notify_request.fcmTokens) == 0: 
            return

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title='Video Enhanced Notification',
                body="Your video has been enhanced. Click here to view it.",
            ),
            tokens=notify_request.fcmTokens,
        )
        response = messaging.send_multicast(message)
        
        print('{0} messages were sent successfully'.format(response.success_count))
