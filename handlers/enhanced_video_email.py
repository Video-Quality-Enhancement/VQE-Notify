from services import EnhancedVideoEmail
from consumers import enhanced_video_notify_consumer

def enhanced_video_email_handler():
    queue = "email_queue"
    routing_key = "#.email.#"
    enhanced_video_email = EnhancedVideoEmail()
    print("starting enhanced video email consumer")
    enhanced_video_notify_consumer(queue, routing_key, enhanced_video_email)
