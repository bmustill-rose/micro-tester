#Import all the modules we'll need
import microbit
import music
import radio
import speech

#Declare all the variables / lists we'll be using
received="" #We'll store each packet we receive from the radio module here. The b means that this variable has a type of byte as opposed to string
lastReceived="lastReceived" #We need to keep track of the last packet we received so that we don't give the user the same direction multiple times which could end up very confusing!
uniqueID=""

radio.on()

def announce(phrase):
 speech.sing("um", speed=138, pitch=24)
 speech.sing("um", speed=138, pitch=24)
 microbit.sleep(250)
 speech.say(phrase)
 if phrase == "destination reached.":
  microbit.sleep(30)
  speech.sing("um", speed=75, pitch=48)
  microbit.sleep(1)
  speech.sing("um", speed=75, pitch=32)
  microbit.sleep(1)
  speech.sing("um", speed=75, pitch=24)
  microbit.sleep(250)


while True:
 received=radio.receive()
 if received != None: #Make sure we've received something
  message=received[5:]
  if uniqueID != received[:4]: #Make sure that what we've received is different to the last time we were here
   uniqueID=received[:4]
   #See if what we've received is something we know about and play sounds accordingly. Remember, we're receiving bytes from the radio module so when we're checking for a match we need to use bytes and not strings
   print(message)
   if message == "1": announce("Walk forw ud.")
   if message == "2": announce("Go up the stairs.")
   if message == "3": announce("Walk through the door.")
   if message == "4": announce("turn left.")
   if message == "5": announce("turn right.")
   if message == "6": announce("destination reached.")
