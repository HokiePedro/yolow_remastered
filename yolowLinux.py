
import Tkinter as tk
from Tkinter import *
#!/usr/bin/env python
import ctypes
import commands
import requests
import sys
import time
import commands

root = tk.Tk()
var = StringVar()
var.set("Battery level: ")
user = None
limit = None

def getName():
    user = entry1.get()
    print user
    return user

def getPercent():
    print entry2.get()
    storPercent = entry2.get()
    limit = float(storPercent)
    return limit


l1 = tk.Label(root, text="Username").grid(row=0)
l2 = tk.Label(root, text="Percent Limit").grid(row=2)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
button1 = tk.Button(root,text="Enter Name",command=getName)
button2 = tk.Button(root,text="Enter Percentage",command=getPercent)
currentPercentage = tk.Label(root,textvariable=var,bg="black",fg="white")

entry1.grid(row=0, column=1)
button1.grid(row=1, columnspan=2)
entry2.grid(row=2, column=1)
button2.grid(row=3,columnspan=2)
entry2.insert(0,0)
currentPercentage.grid(row=4,column=0)

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
     
def getUsername():
    person = raw_input("Enter your username: ");
    return person

def setLimit():
    setLim = input("Battery % to get warnings at (1-100) ")
    numberLim = float(setLim)
    return numberLim

def getBattery():
    choose = True
    status = None
    output = None

    currentPercentLabel = currentPercentage["text"]

    #user = getUsername()
    #limit = setLimit()

    while True:
        time.sleep(3)        
        status = commands.getstatusoutput("cat /sys/class/power_supply/BAT0/status")
        print status
        print status[1]       

        if status[1] == "Charging":
            break
        else:
            #while(user == None and limit ==None):
            #    print "no input"

            root.after(1, getBattery)
            currentPercentLabel = batteryPercent()
            currentPercentLabel = str(currentPercentLabel)

            var.set("Battery level: " + currentPercentLabel) 
            
            root.update_idletasks()    

            compare = batteryPercent()
            print "actual: "
            print compare 
            print "set: "
            print limit

            if limit >= compare:
                print "Yo!"
                yo("07886bd4-b3cb-4107-ba7c-f258118cad51",user)
                break
    
                          
root.after(1, getBattery)
root.mainloop()