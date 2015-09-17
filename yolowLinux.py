#!/usr/bin/env python
import ctypes
import commands
import requests
import sys
import time
import commands

def yo(api_token, username):
    return requests.post("http://api.justyo.co/yo/", data={'api_token': api_token, 'username': username})

def batteryPercent():
    fullBatt = 0
    currBatt = 0
    battPercent = 0
    
#gets full battery level
    fullBattStr = commands.getstatusoutput("cat /sys/class/power_supply/BAT0/charge_full")
#print type(fullBattStr[1])
    fullBatt = float(fullBattStr[1])
#print fullBatt

#gets current battery level
    currBattStr = commands.getstatusoutput("cat /sys/class/power_supply/BAT0/charge_now")
#print currBattStr[1]
#print type(currBattStr[1])
    currBatt = float(currBattStr[1])
         
    battPercent = ("%.2f" % ((currBatt/fullBatt)*100))
    
    currPercent = float(battPercent) 
    stringPercent = str(battPercent)
    finalPercent = (stringPercent + "%")
    #return finalPercent
    return currPercent
        
       
    

def getBattery():
    person = raw_input("Enter your username: ")
    print person
    choose = True
    status = None
    output = None
    setLimit = input("Battery % to get warnings at (1-100) ")
    
    print "set limit time is "
    print type(setLimit)
    print setLimit

    compare = str(setLimit) + ".00%"
    print "You have set your battery warning percentage to " + compare
    
    while True:
        time.sleep(3)        
        status = commands.getstatusoutput("cat /sys/class/power_supply/BAT0/status")
        print status
        print status[1]        
        
        if status[1] == "Charging":
            #do nothiing
            break
        else:
            compare = batteryPercent()
            print "actual: "
            print compare 
            print "set: "
            print setLimit

            if setLimit >= compare:
                print "Yo!"
                yo("07886bd4-b3cb-4107-ba7c-f258118cad51",person)
                break
                        
        
batteryPercent()
getBattery()




