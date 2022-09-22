import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
RECEIVER = "t0924148@u.nus.edu"

message = """\
Suject: Github Action Email Report

This is your daily email report.
"""

context = ssl.create.default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    # server.sendmail(USERNAME, USERNAME, message)
    server.sendmail(USERNAME, RECEIVER, message)
    server.quit()
    print("Successfully sent email")
