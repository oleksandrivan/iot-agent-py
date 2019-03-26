#from bluepy.btle import Peripheral
from time import sleep
from btle import Peripheral, DefaultDelegate, Characteristic
LED_UUID = "19b10001-e8f2-537e-4f6c-d104768a1214"

device = Peripheral("98:4f:ee:0f:2d:89")
characteristics = device.getCharacteristics(uuid=LED_UUID)
characteristic = characteristics[0]
print("Characteristic with uuid {} , value {} and handle {}".format(characteristic.uuid, characteristic.read(),
                                                                    characteristic.getHandle()))
# device.write(data, withResponse=False)
counter = 0
while counter < 20:
    characteristic.write(bytes([1]), withResponse=True)
    sleep(1)
    characteristic.write(bytes([0]), withResponse=True)
    sleep(1)
    counter += 1
device.disconnect()
# print(bytes([1]))
