import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USERNAMME")
    password = os.getenv("PASSWORD")

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as s:
        s.login(username, password)
        s.sendmail(username, receiver, message)

