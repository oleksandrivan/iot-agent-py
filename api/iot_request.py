import requests
import jsonpickle as json

#Useful constants
SERVER_IP = 192.168.0.27
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
    r = requests.post(url,headers=headers, data=json.encode(device,unpicklable=False))
    r.raise_for_status() #Make sure request was succesfull
