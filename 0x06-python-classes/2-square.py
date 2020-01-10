#!/usr/bin/python3
class Square:
    """This is a class Square defined by size."""
    def __init__(self, size=0):
        """The __init__ method of the square class
        Args:
            size: Is the type int private attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
