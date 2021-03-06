
#Contains all the needed entities for creation of houses, sensors and so on
# *Note: the overriden getstate is for adjusting from python class to entity type needed for Fiware
class House:
    def __init__(self, id, address, owner):
        self.type = "House"
        self.id = "urn:ngsi-ld:{}:{}".format(self.type, id)
        self.address = address
        self.owner = owner

        def __getstate__(self):
            state = self.__dict__.copy()
            return state


class Address:
    def __init__(self, street, locality, region, postalCode):
        self.type = "Address"
        self.street = street
        self.locality = locality
        self.region = region
        self.postalCode = postalCode
        self.value = {"street": street,
                      "locality": locality,
                      "region": region,
                      "postalCode": postalCode}

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['street']
        del state['locality']
        del state['region']
        del state['postalCode']
        return state


class Owner:
    def __init__(self, name, age):
        self.type = "Owner"
        self.name = name
        self.age = age
        self.value = {"name": name,
                      "age": age}

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['name']
        del state['age']
        return state


class Service:
    def __init__(self, apikey):
        self.apikey = apikey
        description = {"apikey": apikey,
                       "cbroker": "http://orion:1026",
                       "entity_type": "Thing",
                       "resource": "/iot/d"}
        self.services = [description]

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['apikey']
        return state


class Device:
    def __init__(self, deviceId, mac, number, type, variableName, house):
        self.deviceId = deviceId
        self.type = type
        self.variableName = variableName
        self.house = house
        self.mac = mac
        description = 0
        if type != "Accelerometer":
            description = {"device_id": deviceId,
                           "entity_name": "urn:ngsd-ld:{}:{}".format(type, number),
                           "entity_type": type,
                           "protocol": "PDI-IoTA-UltraLight",
                           "timezone": "Europe/Berlin",
                           "attributes": [{"object_id": variableName, "name": variableName,
                                           "type": "Integer"}],
                           "static_attributes": [{"name": "houseRef", "type": "Relationship",
                                                  "value": house.id}],
                           }
        else:
            description = {"device_id": deviceId,
                           "entity_name": "urn:ngsd-ld:{}:{}".format(type, number),
                           "entity_type": type,
                           "protocol": "PDI-IoTA-UltraLight",
                           "timezone": "Europe/Berlin",
                           "attributes": [{"object_id": "x", "name": "x",
                                           "type": "Float"}, {"object_id": "y", "name": "y",
                                           "type": "Float"}, {"object_id": "z", "name": "z",
                                           "type": "Float"}],
                           "static_attributes": [{"name": "houseRef", "type": "Relationship",
                                                  "value": house.id}],
                           }
        self.devices = [description]

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['deviceId']
        del state['mac']
        del state['type']
        del state['variableName']
        del state['house']
        return state


FRONT_END_URL = "http://192.168.0.14:5000/api/world"

#The subscriptions changes based on the type of sensor
class Subscription:
    def __init__(self, type, variableName):
        self.description = "Notification of changed variable"
        if type == "Accelerometer":
            self.subject = {"entities": [{"idPattern": ".*", "type": type}], "condition": {
                "attrs": ["x", "y", "z"]
            }}
        else:
            self.subject = {"entities": [{"idPattern": ".*", "type": type}], "condition": {
                "attrs": [variableName]
            }}
        self.notification = {"http": {"url": FRONT_END_URL}}

    def __getstate__(self):
        state = self.__dict__.copy()
        return state
