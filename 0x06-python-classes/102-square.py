#!/usr/bin/python3
class Square:
    """This is a class Square defined by size."""
    def __init__(self, size=0):
        """The __init__ method of the square class
        Args:
            size: Is the type int private attribute
        """
        self.size = size

    @property
    def size(self):
        """Private instance attribute getter method."""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Private instance attribute property setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """The area public instance method of the square class"""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Compare if the area of a square is equal to other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if the area of a square is diferent to other"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of a square is less than other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of a square is less than or equal other"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of a square is greater than to other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of a square is greater than or equal other"""
        return self.area() >= other.area()
