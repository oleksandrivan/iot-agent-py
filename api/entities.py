
class House:
  def __init__(self, id, address,owner):
    self.id = id
    self.type = "House"
    self.address = address
    self.owner = owner

class Address:
  def __init__(self, street, locality,region,postalCode):
    self.street = street
    self.type = "Address"
    self.locality = locality
    self.region = region
    self.postalCode = postalCode

class Owner:
  def __init__(self, name, age):
    self.name = name
    self.type = "Owner"
    self.age = age

class Service:
    def __init__(self, apikey):
        description = {"apikey" : apikey,
        "cbroker" : "http://orion:1026",
        "entity_type" : "Thing",
        "resource" : "/iot/d" }
        self.services = [description]

class Device:
    def __init__(self, deviceId, type, variableName,house):
        description = {"device_id" : deviceId,
        "entity_name" : house.id +":"+ deviceId,
        "entity_type" : type,
        "protocol" : "PDI-IoTA-UltraLight",
        "timezone" : "Europe/Berlin" ,
        "attributes" : [ { "object_id" : variableName, "name" : variableName,
        "type" : "Integer"  } ],
        "static_attributes" : [ {"name" : "houseRef" , "type" : "Relationship",
        "value" : house.id } ],
        }
        self.devices = [description]
