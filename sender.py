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

def startBroadcasting(broadcastPower):
 display.clear()
 radio.config(power=broadcastPower)
 i=0
 print(i)
 display.show(str(i),delay=250,clear=True,wait=True)
 radio.send(i)
 while True:
  sleep(100) #Debounce
  if button_a.was_pressed():
   i-=1
   print(i)
   display.show(str(i),delay=250,clear=True,wait=True)
   radio.send(i)
  if button_b.was_pressed():
   i+=1
   print(i)
   display.show(str(i),delay=250,clear=True,wait=True)
   radio.send(i)

message="Select my broadcast power using button a then press button b to continu"
print(message)
display.scroll(message,delay=100,wait=false)
while True:
 while broadcastPower == "":
  if button_a.was_pressed():
   print("Select broadcast power")
   broadcastPower=selectBroadcastPower()
 startBroadcasting(broadcastPower)