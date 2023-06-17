from services import PushNotification
from consumers import enhanced_video_notify_consumer

def fcm_handler():
    queue = "ui_queue"
    routing_key = "#.ui.#"
    pushn = PushNotification()
    print("starting enhanced video email consumer")
    enhanced_video_notify_consumer(queue, routing_key, pushn)
