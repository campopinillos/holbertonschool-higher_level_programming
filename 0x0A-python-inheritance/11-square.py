#!/usr/bin/python3
"""
Square module

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass Square from class Rectangle"""

    def __init__(self, size):
        """Instantiation, constructor"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area method"""
        return (self.__size * self.__size)

    def __str__(self):
        """Print"""
        return ('[Square] {}/{}'.format(str(self.__size),
                                        str(self.__size)))
