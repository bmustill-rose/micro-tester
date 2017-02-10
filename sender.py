from microbit import *
import radio

def selectBroadcastPower():
 display.clear()
 i=0
 print(i)
 while True:
  display.show(str(i), wait=False)
  if button_b.was_pressed():
   return i
  if button_a.was_pressed():
   i=i+1
   if i > 7: i=0
   display.clear()
   print(i)

def startBroadcasting(broadcastPower :int, objectID :int):
 random.seed(running_time())
 uniqueID=str(random.randint(4502,9999))
 stringToSend=str(uniqueID)+":"+str(objectID+1) #Do the +1 because the receiver starts at 1
 messageToPrint="I am broadcasting "+objectIDs[objectID]+", at a power level of "+str(broadcastPower)+", with a unique ID of "+str(uniqueID)+"."
 print(messageToPrint)
# display.scroll(messageToPrint, delay=100, wait=True)
 sleep(750)
 display.clear()
 radio.config(power=broadcastPower, length=8)
 while True:
  radio.send(stringToSend)
  sleep(250)


button_a.was_pressed()
button_b.was_pressed()
print("In main")
while True:
 display.scroll("Select my broadcast power using button a then press b to continue.", delay=100, wait=False)
 while broadcastPower == "":
  if button_a.was_pressed():
   print("Select broadcast power")
   broadcastPower=selectBroadcastPower()
 display.clear()
 display.scroll("Select the object that I should represent using button a then press b to continue", delay=100, wait=False)
 while objectID == "":
  if button_a.was_pressed():
   print("Select object")
   objectID=selectObjectID()
 display.clear()
 startBroadcasting(broadcastPower, objectID)