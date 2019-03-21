
class House:
  def __init__(self, id, address,owner):
    self.type = "House"
    self.id = "urn:ngsi-ld:{}:{}".format(self.type,id)
    self.address = address
    self.owner = owner

    def __getstate__(self):
      state = self.__dict__.copy()
      return state

class Address:
    def __init__(self, street, locality,region,postalCode):
        self.type = "Address"
        self.street = street
        self.locality = locality
        self.region = region
        self.postalCode = postalCode
        self.value = {"street" : street,
        "locality" : locality ,
        "region" : region,
        "postalCode" : postalCode}

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
      self.value = {"name" : name,
      "age" : age}

  def __getstate__(self):
    state = self.__dict__.copy()
    del state['name']
    del state['age']
    return state

class Service:
    def __init__(self, apikey):
        self.apikey = apikey
        description = {"apikey" : apikey,
        "cbroker" : "http://orion:1026",
        "entity_type" : "Thing",
        "resource" : "/iot/d" }
        self.services = [description]

    def __getstate__(self):
      state = self.__dict__.copy()
      del state['apikey']
      return state

class Device:
    def __init__(self, deviceId,number,type, variableName,house):
        self.deviceId = deviceId
        self.type = type
        self.variableName = variableName
        self.house = house
        description = {"device_id" : deviceId,
        "entity_name" : "urn:ngsd-ld:{}:{}".format(type,number),
        "entity_type" : type,
        "protocol" : "PDI-IoTA-UltraLight",
        "timezone" : "Europe/Berlin" ,
        "attributes" : [ { "object_id" : variableName, "name" : variableName,
        "type" : "Integer"  } ],
        "static_attributes" : [ {"name" : "houseRef" , "type" : "Relationship",
        "value" : house.id } ],
        }
        self.devices = [description]
    def __getstate__(self):
      state = self.__dict__.copy()
      del state['deviceId']
      del state['type']
      del state['variableName']
      del state['house']
      return state
