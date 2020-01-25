#!/usr/bin/python3
"""
Base Model

"""
import json
import os


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
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_str))

    @staticmethod
    def from_json_string(json_string):
        file = []
        if json_string is not None:
            file = json.loads(json_string)
        return file

    @classmethod
    def create(cls, **dictionary):
        ins = None
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        elif cls.__name__ == "Square":
            ins = cls(1)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        file = "{}.json".format(cls.__name__)
        l_d = []
        if os.path.exists(file):
            with open(file, 'r') as f:
                l_d = [cls.create(**d) for d in cls.from_json_string(f.read())]
        return l_d
