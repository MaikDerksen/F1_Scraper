# message.py
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_whatsapp_messageT(summary_filename):
    # Your Account SID and Auth Token from Twilio
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Read the summary
    with open(summary_filename, 'r', encoding='utf-8') as file:
        summary = file.read()

    # Send a WhatsApp message
    message = client.messages.create(
        body=summary,
            from_=os.getenv('TWILIO_WHATSAPP_FROM'),
            to=os.getenv('TWILIO_WHATSAPP_TO')
    )

    print(f"WhatsApp message sent. SID: {message.sid}")