import requests
import jsonpickle as json

#Useful constants
SERVER_IP = "192.168.0.27"
ORION_PORT = 1026
IOT_AGENT_PORT = 4041
IOT_HTTP_PORT = 7896

def checkStatus():
    #Check connection to Orion
    url = "http://{}:{}/version/".format(SERVER_IP,ORION_PORT)
    r = requests.get(url)
    r.raise_for_status()
    #Check connection to IoT Agent
    url = "http://{}:{}/iot/about".format(SERVER_IP,IOT_AGENT_PORT)
    r = requests.get(url)
    r.raise_for_status()
    print("Connection succesfull")



def addHouse(house):
    url = "http://{}:{}/v2/entities/".format(SERVER_IP,ORION_PORT)
    headers = {"Content-Type":"application/json"}
    data = json.encode(house,unpicklable=False)
    r = requests.post(url,headers=headers, data=data)
    r.raise_for_status() #Make sure request was succesfull

def startService(service):
    url = "http://{}:{}/iot/services".format(SERVER_IP,IOT_AGENT_PORT)
    headers = {"Content-Type":"application/json",
    "fiware-service" : "openiot", "fiware-servicepath":"/"}
    data = json.encode(service,unpicklable=False)
    r = requests.post(url,headers=headers, data=data)
    r.raise_for_status() #Make sure request was succesfull

def addDevice(device):
    url = "http://{}:{}/iot/devices".format(SERVER_IP,IOT_AGENT_PORT)
    headers = {"Content-Type":"application/json",
    "fiware-service" : "openiot", "fiware-servicepath":"/"}
    data = json.encode(device,unpicklable=False)
    r = requests.post(url,headers=headers, data=data)
    r.raise_for_status() #Make sure request was succesfull

def sendReading(service,device,reading):
    url = "http://{}:{}/iot/d".format(SERVER_IP,IOT_HTTP_PORT)
    params = { "k": service.apikey, "i" : device.deviceId }
    headers = {"Content-Type":"text/plain"}
    data = device.variableName + "|"+ str(reading)
    r = requests.post(url,headers=headers, params=params,data=data)
    r.raise_for_status() #Make sure request was succesfull
