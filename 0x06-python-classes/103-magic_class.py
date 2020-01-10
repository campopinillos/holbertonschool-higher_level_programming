#!/usr/bin/python3
class MagicClass:
    import math

    def __init__(self, radious=0):
        self.__radious = radious
        if (type(radious) is not int or
                type(radious) is not float):
            raise TypeError('radius must be a number')

    def area(self):
        return((self.__radious ** 2) * math.pi)

    def circumference(self):
        return(2 * math.pi * self.__radious)
