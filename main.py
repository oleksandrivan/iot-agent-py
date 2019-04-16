from api import entities as ntt
from api import iot_request as request
from api import bluetooth as blue
import jsonpickle as json
import secrets
import time
from bluepy.btle import Scanner, DefaultDelegate



address = ntt.Address("Rioja", "Leganes", "Madrid", "28915")
owner = ntt.Owner("Carla", 75)
house = ntt.House(1, address, owner)
service = ntt.Service(secrets.token_urlsafe(16))
door = ntt.Device("door", "ac:9a:22:9b:66:a2", 1, "Door", "reading", house)
presence = ntt.Device("presence", "ac:9a:22:93:59:d6", 1, "Presence", "reading", house)
doorSubscription = ntt.Subscription("Door","reading")
presenceSubscription = ntt.Subscription("Presence","reading")

listDevice = [door, presence]

#Fiware entities initialization
request.checkStatus()
request.startService(service)
request.addHouse(house)
request.addDevice(door)
request.addDevice(presence)
request.registerSubscription(doorSubscription)
request.registerSubscription(presenceSubscription)

#Bluetooth readings

scanner = Scanner().withDelegate(blue.ScanDelegate(listDevice, service))
while True:
    print("Scanning...")
    scanner.scan(10, passive=True)