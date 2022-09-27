import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
RECEIVER = "t0924148@u.nus.edu"

message = """\
Suject: Email News

This is your weekly email report from Homey.com.sg

1. New project launching in Singapore
2. Singapore rental market update
3. HDB resale price update
4. Bank Loan / interest rate update
"""

context = ssl.create.default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, RECEIVER, message)
    server.quit()
    print("Successfully sent email")
