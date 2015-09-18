import serial
import Tkinter
from Tkinter import *
import tkMessageBox
import time
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import style
import matplotlib.pyplot as mp
import Tkinter as T, sys
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

style.use('ggplot')


timout = 5000

import Tkinter as tk

root = tk.Tk()

def send_go():
    try:
        port = "/dev/ttyUSB1"
        ser = serial.Serial(port, 115200)
    except serial.serialutil.SerialException:
        ser = serial.Serial('/dev/ttyUSB2',115200)  # open first serial port

    ser.write("11111111")
    print "Go"

def send_stop():
    try:
        port = "/dev/ttyUSB1"
        ser = serial.Serial(port, 115200)
    except serial.serialutil.SerialException:
        ser = serial.Serial('/dev/ttyUSB2',115200)  # open first serial port
    ser.write("11111000")
    print "Stop"

#Sensor data labels on the right
altitude = tk.Label(root, text="Altitude: ",bg="black",fg="red")
altitude.grid(column=21,row=0,columnspan=10,rowspan=5)

lrdistance = tk.Label(root, text="Left wall distance: ",bg="black",fg="white")
lrdistance.grid(column=21,row=5,columnspan=10,rowspan=5)

rightdistance = tk.Label(root, text="Right wall distance: ",bg="black",fg="white")
rightdistance.grid(column=21,row=10,columnspan=10,rowspan=5)

stability = tk.Label(root, text="Stability: ",bg="black",fg="blue")
stability.grid(column=21,row=15,columnspan=10,rowspan=5)
#end sensor data labels

# go button
go = tk.Button(root, text="Go", command = send_go)
go.grid(column=24,row=20,columnspan=3,rowspan=3)
#end go button

# stop button
stop = tk.Button(root, text="Stop", command = send_stop)
stop.grid(column=24,row=23,columnspan=3,rowspan=3)
#end go button

#canvas top
mainCanvas = tk.Canvas(bg="blue",width=800,height=250)
mainCanvas.grid(column=0,row=0,rowspan=15,columnspan=20)
#canvas close

#canvas bottom
bottomCanvas = tk.Canvas(bg="red",width=800,height=250)
bottomCanvas.grid(column=0,row=16,rowspan=15,columnspan=20)
#bottom canvas close

globvar = 0
xincrease = 1
xlincrease = 1
heightAlt = 0
xglobalvar = 0
yglobalvar = 0
yincrease = 1

fig = None

def update_status():

    
    current_status = altitude["text"]

    try:
        port = "/dev/ttyUSB1"
        ser = serial.Serial(port, 115200)
    except serial.serialutil.SerialException:
        ser = serial.Serial('/dev/ttyUSB2',115200)  # open first serial port

    
    
    value = ser.read(8)
    print value
    firsttwobits = value[0:2]
    if firsttwobits == '00': #for left sensor
        global xglobalvar

        global globvar

        global xlincrease
        global heightAlt
        
        xlincrease = xlincrease + 1

        plt.figure(1)
        plt.axis([0, 16 , 0, xlincrease])
        plt.ion()
        
        print value[2:8]
        lastSixBits = value[2:8]
        binToLeftDist = int(lastSixBits,2)
        print binToLeftDist

        binToStatus = str(binToLeftDist)
        current_status = binToStatus

        lrdistance["text"] = "Distance \n From Left Wall: \n (centimeters) \n" + current_status

        plt.show()
        plt.scatter(binToLeftDist, xglobalvar)
        plt.draw()
        plt.ylabel('distance traveled')
        plt.xlabel('distance from wall (left)')
        global fig
        xglobalvar = xglobalvar + 1
        
    elif firsttwobits == '01': #for right sensor
        global yglobalvar
        global yincrease
        
        yincrease = yincrease + 1
        
        plt.figure(2)
        plt.axis([0, 16 , 0, yincrease])
        plt.ion()

        print value[2:8]
        lastSixBits = value[2:8]
        binToRightDist = int(lastSixBits,2)
        print binToRightDist

        binToStatus = str(binToRightDist)
        current_status = binToStatus        

        rightdistance["text"] = "Distance \n From Right Wall: \n (centimeters) \n" + current_status

        plt.show()
        plt.scatter(binToRightDist, yglobalvar)
        plt.draw()
        plt.ylabel('distance traveled')
        plt.xlabel('distance from wall (right)')
        global fig
        yglobalvar = yglobalvar + 1

    elif firsttwobits == '10': #altitide
        global globvar

        global xincrease
        global heightAlt
        xincrease = xincrease + 1

        plt.figure(3)
        plt.axis([0, xincrease , 0, 50])
        plt.ion()
        
        print value[2:8]
        lastSixBits = value[2:8]
        heightAlt = int(lastSixBits,2)
        print heightAlt
        binToStatus = str(heightAlt)
        current_status = binToStatus        
        altitude["text"] = "Altitiude: \n (centimeters) \n" + current_status
        print globvar
        print heightAlt

        plt.show()
        plt.scatter(globvar, heightAlt)
        plt.draw()
        plt.ylabel('altitude')
        plt.xlabel('distance traveled')
        global fig
        globvar = globvar + 1
    else:
        print 'stability'
    
        
    #current_status = value

    root.after(100, update_status)

root.after(1,update_status)
root.mainloop()
