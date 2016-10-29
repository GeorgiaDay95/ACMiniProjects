from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("/dev/cu.usbmodem1411",9600,timeout=2)

# randomID = random()
client = Mosquitto("GeorgiaDay95")
client.connect("10.212.61.136")
client.subscribe("/lights")

# The rest of your code goes in here !!!


def messageReceived(broker, obj, msg):
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    
    if (payload == "ON"):
        message = "1"
    if (payload == "OFF"):
        message = "0"
    board.write(message.encode())
    
    

client.on_message = messageReceived

 # While the client still exists, ask it to process incoming messages
while (client != None): client.loop()