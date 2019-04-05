from bluepy import btle
from bluepy.btle import Peripheral

SERVICE_UUID = "19b10000-e8f2-537e-4f6c-d104768a1214"
LED_UUID = "19b10001-e8f2-537e-4f6c-d104768a1214"


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print('notification arrived with data {}'.format(data))


# Initialisation  -------

p = Peripheral("98:4f:ee:0f:2d:89")
p.withDelegate(MyDelegate())

services = p.getServices()
characteristics = p.getCharacteristics()

for x in services:
    print("Service uuid {}".format(x.uuid))

for x in characteristics:
    print("Characteristic uuid {} with properties {}".format(x.uuid, x.propertiesToString()))


svc = p.getServiceByUUID(SERVICE_UUID)
ch = svc.getCharacteristics()[0]
print("Notify value is {}".format(p.readCharacteristic(ch.getHandle()+1)))
p.writeCharacteristic(ch.getHandle()+1, b'\x01\x00', withResponse=True)
print("New notify value is {}".format(p.readCharacteristic(ch.getHandle()+1)))
print("Actual value is {}".format(p.readCharacteristic(ch.getHandle())))


while True:
    if p.waitForNotifications(1.0):
        continue

    print("Waiting...")