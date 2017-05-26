#!/usr/bin/env python

import os
import time
import requests
import json
import smtplib
import ConfigParser as cfg


directory = os.path.dirname(os.path.realpath(__file__))

#Read configuration.ini to get gmail username and password
Config = cfg.ConfigParser()
Config.read( directory+"/configuration.ini")
EMAIL = Config.get("login","gmail_username")
PASS = Config.get("login","password")

#Set the delay in seconds for the script to wait in between steps
DELAY = 2

#Gets the ip address of the ethernet port
def getEth0IP():
    ipString = os.popen("ifconfig eth0 | grep \"inet addr:\"").read()
    if ipString:
        ipStringArray= ipString.split(":")
        ipStringArray= ipStringArray[1].split(" ")
        return ipStringArray[0]
    return "not connected"

#Gets the ip address of the wireless connection
def getWlan0IP():
    ipString = os.popen("ifconfig wlan0 | grep \"inet addr:\"").read()
    if ipString:
        ipStringArray= ipString.split(":")
        ipStringArray= ipStringArray[1].split(" ")
        return ipStringArray[0]
    return "not connected"

#Wait 2 seconds then start ngrok
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
