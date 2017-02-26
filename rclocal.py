#!/usr/bin/env python

#This adds start-server.py to the file /etc/rc.local
#This causes the script to run at boot
import os

dirPath = os.path.dirname(os.path.realpath(__file__))

command = 'python '+dirPath+'/start-server.py &';
fileName = '/etc/rc.local'

#open the file and read the all the lines into the list content
with open(fileName,"rw") as f:
    content = f.readlines()

#This adds the command which starts the server to the list content
lineCount = 0
for line in content:
    if line == command+"\n":
        print command+" already installed"
        f.close()
        exit()
    if line == "exit 0\n":
        #add the command to the content list and then exit out
        content.insert(lineCount,command+"\n")
        f.close()
        break
    lineCount+=1

#open the file again so that it can be replace with the list content
f = open(fileName,"w")
for line in content:
    f.write(line)
