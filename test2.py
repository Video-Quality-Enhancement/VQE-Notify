import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
# from dotenv import load_dotenv

# load_dotenv()
cred = credentials.Certificate("./auth/firebase.sa.key.json")
app = firebase_admin.initialize_app(cred)


registration_tokens = [
    "ejXDRWDoY6M9iOj7oc_5wZ:APA91bEc2RKpj7uP5sULqsSZ1d3-QUBgiDiyOo9AM56KJugCLSXu-J-dtKnwdfEarLMjaG8s-Aiwbuzm6taPeF6_6LXc6gNjyTsEPsOKYBfunTncQiqsFlqk4ZFOPz7Woi-S7fs6BDzm",
]

message = messaging.MulticastMessage(
    notification=messaging.Notification(
        title='Video Enhanced Notification',
        body="Your video has been enhanced. Click here to view it.",
    ),
    tokens=registration_tokens,
)
response = messaging.send_multicast(message)
# See the BatchResponse reference documentation
# for the contents of response.
print('{0} messages were sent successfully'.format(response.success_count))

