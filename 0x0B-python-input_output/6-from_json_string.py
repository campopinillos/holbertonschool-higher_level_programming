#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Function that returns the JSON representation of an object (string)
    """
    file = json.loads(my_str)
    return file
