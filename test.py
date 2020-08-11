#!/usr/bin/python3

from models.base_model import BaseModel
from models.city import City
import models

ciudad = City()
print(models.storage.all())
# models.storage.new(ciudad)
# print(models.storage.all())
# models.storage.save()
# print(ciudad)
# print(ciudad.to_dict())
