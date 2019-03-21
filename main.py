from api import entities as ntt
from api import iot_request as request
# address = ntt.Address("Rioja","Leganes","Madrid","28915")
# owner = ntt.Owner("Carlos",75)
# house = ntt.House("house001",address,owner)
# service = ntt.Service("sesamo")
# device = ntt.Device("sensor1", "Presence", "counter", house)
#
# encoded = json.encode(device,unpicklable=False)
#
# print(encoded)

request.checkStatus()
