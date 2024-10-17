import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

def send_email(summary_filename):
    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # Your Gmail credentials (loaded from environment variables)
    gmail_user = os.getenv('GMAIL')
    gmail_password = os.getenv('GMAIL_APP')

    # Email addresses
    from_email = gmail_user
    to_email = os.getenv("GMAIL")

    # Read the summary content
    with open(summary_filename, 'r', encoding='utf-8') as file:
        summary = file.read()

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Summary of Latest Motorsport Articles'

    # Attach the summary content as the body of the email
    msg.attach(MIMEText(summary, 'plain'))

    try:
        # Connect to the Gmail server and send the email
        smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_password)
        smtpserver.sendmail(from_email, to_email, msg.as_string())
        smtpserver.quit()

        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")
