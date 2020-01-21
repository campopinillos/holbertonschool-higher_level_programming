#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)
    """
    file = json.dumps(my_obj)
    return file
