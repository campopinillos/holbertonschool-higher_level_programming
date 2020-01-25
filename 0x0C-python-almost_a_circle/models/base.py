#!/usr/bin/python3
"""
Base Model

"""
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        list_str = []
        if list_objs is not None:
            list_str = [l.to_dictionary() for l in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as new_file:
            new_file.write(cls.to_json_string(list_str))

    @staticmethod
    def from_json_string(json_string):
        file = []
        if json_string is not None:
            file = json.loads(json_string)
        return file

    @classmethod
    def create(cls, **dictionary):