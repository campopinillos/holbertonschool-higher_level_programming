#!/usr/bin/python3
"""
Student Class

"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Instantiation, constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method retrieves a dictionary representation of a
        Student instance
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Public method replaces all attributes of the Student instance
        """
        [setattr(self, key, value) for key, value in json.items()]
