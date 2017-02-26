#!/usr/bin/env python
import os

dirPath = os.path.dirname(os.path.realpath(__file__))

command = 'python '+dirPath+'/start-server.py &';
fileName = '/etc/rc.local'

with open(fileName,"rw") as f:
    content = f.readlines()

lineCount = 0
for line in content:
    if line == command+"\n":
        print command+" already installed"
        f.close()
        exit()
    if line == "exit 0\n":
        content.insert(lineCount,command+"\n")
        f.close()
        break
    lineCount+=1

file2 = open(fileName,"w")
for line in content:
    file2.write(line)
