#!/usr/bin/env python3
import sys
import platform

hostname = platform.node()
while True:
    peeter = input(" ")
    idk = peeter.split(' ')
    if idk[0] == "what":
        if idk[1] == "is":
            if idk[2] == "your":
                if idk[3] == "name":
                    print ("My name is ", hostname)
    else:
        if idk[0] == "stop":
            sys.exit(0)
