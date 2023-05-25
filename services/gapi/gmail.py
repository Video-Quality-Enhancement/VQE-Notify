import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
from email.message import EmailMessage


class Gmail:

    def get_creds(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        creds = None

        if os.path.exists('./auth/token.json'):
            creds = Credentials.from_authorized_user_file('./auth/token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('./auth/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('./auth/token.json', 'w') as token:
                token.write(creds.to_json())

        return creds


    def send(self, to_email: str, subject: str, body: str):
        creds = self.get_creds()

        try:
            service = build('gmail', 'v1', credentials=creds)
            message = EmailMessage()

            message.set_content(body)

            message['To'] = to_email
            message['From'] = 'vqe.ai.cp@gmail.com'
            message['Subject'] = subject

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            create_message = {
                'raw': encoded_message
            }

            send_message = service.users().messages().send(userId="me", body=create_message).execute()
            print(F'Message Id: {send_message["id"]}')

        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None
        return send_message