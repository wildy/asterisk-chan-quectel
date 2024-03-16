#!/usr/bin/env python
import os, smtplib, ssl, configparser, argparse
from email.mime.text import MIMEText

relpath = os.path.dirname(__file__)
config = configparser.ConfigParser()
config_file = os.path.join(relpath, 'sms2email.conf')
config.read(config_file)

server = config['mail']['server']
port = config['mail']['port']
username = config['mail']['username']
password = config['mail']['password']
sender = config['mail']['sender']
sender_name = config['mail']['sender_name']

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--channel', nargs=1, required=True)
parser.add_argument('-n', '--callerid', nargs=1, required=True)
# parser.add_argument('-o', '--own-number', nargs=1, required=False)
parser.add_argument('-d', '--destination', nargs=1, required=True)

args = parser.parse_args()

buffer = []
while True:
    try:
        line = input()
    except EOFError:
        break
    buffer.append(line)


# Create a secure SSL context
context = ssl.create_default_context()

message = f"""\
From: {sender_name} <{sender}>
To: <{args.destination[0]}>'
Subject: Incoming SMS from {args.callerid[0]}

Incoming SMS from {args.callerid[0]} on channel {args.channel[0]}:

"""

message = message + format("\n".join(buffer))

with smtplib.SMTP_SSL(server, port, context=context) as server:
    server.login(username, password)
    server.sendmail(sender, args.destination, message)