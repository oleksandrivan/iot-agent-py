from api import entities as ntt
from api import iot_request as request
import jsonpickle as json
import secrets
import time

address = ntt.Address("Rioja","Leganes","Madrid","28915")
owner = ntt.Owner("Carla",75)
house = ntt.House(1,address,owner)
service = ntt.Service(secrets.token_urlsafe(16))
device = ntt.Device("sensor1",1,"Presence", "counter", house)

# encoded = json.encode(house,unpicklable=False)
# print(encoded)

request.checkStatus()
request.startService(service)
# request.addHouse(house)
# request.addDevice(device)
# time.sleep(10)
for i in range(10):
    time.sleep(1)
    request.sendReading(service,device,i)
