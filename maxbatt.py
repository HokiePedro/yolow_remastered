import commands

#gives you the full battery level of your computer
import commands

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
    print type(battPercent)
     
    currPercent = float(battPercent) 
 #print currPercent
    stringPercent = str(battPercent)
    finalPercent = (stringPercent + "%")
    #return finalPercent
    print battPercent
    return currPercent

batteryPercent()

        