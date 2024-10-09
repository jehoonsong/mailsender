#!/usr/bin/env python3

import smtplib
import argparse
import sys
from email.mime.text import MIMEText

def main():
    parser = argparse.ArgumentParser(description="Send an email from Colab")
    parser.add_argument("title", help="The subject of the email")
    parser.add_argument("--text", default="Sent from Colab!", help="The body of the email")
    args = parser.parse_args()

    # Set up the email details
    with open('/content/.user_email', 'r') as file:
        receiver = file.read().strip()

    sender = receiver

    with open('/content/.gmail_app_password', 'r') as file:
        password = file.read().strip()

    # Create the email
    msg = MIMEText(args.text)
    msg["Subject"] = args.title
    msg["From"] = sender
    msg["To"] = receiver

    # Send the email using Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

    print("Email sent successfully!")

if __name__ == "__main__":
    main()