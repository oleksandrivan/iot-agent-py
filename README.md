# IoT Agent communication with Python
[![Python 3.7.3+](https://img.shields.io/badge/Python-3.7.3+-blue.svg)](https://www.python.org/downloads/release/python-373/)


This part is responsible for entity creation, as well as forwarding information from BLE to Ultralight 2.0 protocol
## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash
pip install -r requirements.txt 
```
## Previuos work
### Set enviroment IPs 

Set the current IP and port values in the next files
* api/iot_request.py 
  * SERVER_IP = "192.168.0.27"
  * ORION_PORT = 1026
  * IOT_AGENT_PORT = 4041
  * IOT_HTTP_PORT = 7896
* api/entities.py
  * FRONT_END_URL = "http://192.168.0.14:5000/api/world"
### Set entities to create 
By default the next entities will be created, change **main.py** as needed.
```python
address = ntt.Address("Rioja", "Leganes", "Madrid", "28915")
owner = ntt.Owner("Carla", 75)
house = ntt.House(1, address, owner)
service = ntt.Service(secrets.token_urlsafe(16))
door = ntt.Device("door", "ac:9a:22:9b:66:a2", 1, "Door", "reading", house)
presence = ntt.Device("presence", "ac:9a:22:93:59:d6", 1, "Presence", "reading", house)
accelerometer = ntt.Device("accelerometer", "98:4f:ee:0f:2d:89", 1, "Accelerometer", None , house)
doorSubscription = ntt.Subscription("Door", "reading")
presenceSubscription = ntt.Subscription("Presence", "reading")
accelerometerSubscription = ntt.Subscription("Accelerometer", None )
```
## Usage

To run the code, automatically creates entities in Fiware and starts to scan for the Bluetooth sensors 
```bash
sudo python3 main.py
```
