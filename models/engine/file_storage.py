#!/usr/bin/python3


""" Convert the dictionary representation to a JSON string """
import json
import os
from models.base_model import BaseModel


class FileStorage:
     """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """ all method that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ new method sets in __objects the obj with
        key <obj class name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ save method serializes __objects to the JSON file
        (path: __file_path) """
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            new_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_d, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised) """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
