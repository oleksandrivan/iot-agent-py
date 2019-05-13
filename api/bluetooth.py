from bluepy.btle import Scanner, DefaultDelegate
from api import iot_request as request
from time import sleep
import struct

class ScanDelegate(DefaultDelegate):
    fiwareService = 0
    x,y,z = 0, 0, 0
    def __init__(self, listDevices, fiwareService):
        DefaultDelegate.__init__(self)
        self.listDevices = listDevices
        ScanDelegate.fiwareService = fiwareService

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewData:
            for device in self.listDevices:
                if dev.addr == device.mac:
                    ScanDelegate.processDevice(self, device, dev.rawData)


    def processDevice(self, device, rawData):
        if device.type == "Door":
            state = rawData[20]
            if state == 0x00:
                print('Door closed')
                request.sendReading(ScanDelegate.fiwareService, device, 0)
            if state == 0x02:
                print('Door open')
                request.sendReading(ScanDelegate.fiwareService, device, 1)
        elif device.type == "Presence":
            state = rawData[20]
            if state == 0x03:
                print("Movement detected")
                request.sendReading(ScanDelegate.fiwareService, device, 1)
                sleep(3)
                request.sendReading(ScanDelegate.fiwareService, device, 0)
        elif device.type == "Accelerometer":
            [ax,ay,az] = struct.unpack('fff', rawData[13:])
            if ScanDelegate.x != ax or ScanDelegate.y != ay or ScanDelegate.z != az:
                print("Accelerometer detected")
                ScanDelegate.x = ax
                ScanDelegate.y = ay
                ScanDelegate.z = az
                request.sendReadingAccel(ScanDelegate.fiwareService, device, ax, ay, az)

        else:
            print("Unsupported device type {}".format(device.type))
