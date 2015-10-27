#!/usr/bin/python

import time
# Simple python application

#Prints out a helloworld message
print("Hello from python! Taking a 10 minute power nap now.")

# Sleeps for 10 minutes
for x in range(0, 600):
    print ("I've been asleep for %d seconds now..." % (x))
    time.sleep(1)

# Exiting now..
print ("Woke up! Exiting application now.")