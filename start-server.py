#!/usr/bin/env python

import os
import time
import requests
import json
import smtplib

############################################
EMAIL = "YOUR_GMAIL_EMAIL"
PASS = "YOUR_GMAIL_PASS"
############################################

DELAY = 10

def getEth0IP():
    ipString = os.popen("ifconfig eth0 | grep \"inet addr:\"").read()
    ipStringArray= ipString.split(":")
    ipStringArray= ipStringArray[1].split(" ")
    return ipStringArray[0]


def getWlan0IP():
    ipString = os.popen("ifconfig wlan0 | grep \"inet addr:\"").read()
    ipStringArray= ipString.split(":")
    ipStringArray= ipStringArray[1].split(" ")
    return ipStringArray[0]

directory = os.path.dirname(os.path.realpath(__file__))
print directory

#Wait DELAY number of seconds then start ngrok
time.sleep(DELAY)
os.system(directory + '/ngrok http 80 -log=stdout > /dev/null &')

#Wait 2 seconds then get the url of the ngrok website
time.sleep(2)
r = requests.get('http://localhost:4040/api/tunnels/command_line')
rJson = r.json()
publicURL = rJson['public_url']

#Convert the json data to a string and parse it
stringPublicURL = str(publicURL)
stringPublicURL = stringPublicURL[8:len(publicURL)]

#Send yourself an email with the url in it 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL, PASS)
server.sendmail(EMAIL, EMAIL, 
'\nhttp://'+
stringPublicURL+
'/html\n\nWireless IP: '+
getWlan0IP()+
'\n\nWired IP: '+
getEth0IP())
server.quit()
