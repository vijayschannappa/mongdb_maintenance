#!Email Sender

#! EMAIL SENDER

import smtplib
import pandas as pd
import importlib
import datetime
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


username = "rrf@energy.com"
password = "****"  # Password
server = smtplib.SMTP('smtp.gmail.com', 587)


from_addrs = "*.com"

to_addrs = '*.com,*.nair@.com'


def send_mail(username, password, msg):
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    print('logged in')
    server.sendmail(from_addrs, to_addrs.split(","), msg.as_string())
    server.quit()


def alert_mail_sender(alert):
    msg = MIMEMultipart()
    msg['Subject'] = "MONGOD SERVICE ALERT"
    msg['From'] = from_addrs
    msg['To'] = to_addrs
    body = MIMEText(alert, 'html')
    msg.attach(body)

    try:
        send_mail(username, password, msg)
        print("ALERT MAIL SENT SUCCESSFULLY")
    except Exception as e:
        print(f'SMTPAuthenticationError: {e}')
