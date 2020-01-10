#!/usr/bin/python3
class Square:
    """This is a class Square defined by size."""
    def __init__(self, size=0):
        """The __init__ method of the square class
        Args:
            size (int): Private attribute
        """
        self.size = size

    @property
    def size(self):
        """Private instance attribute getter method.
        Returns:
            property: Private attribute size
        """
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
        """The area public instance method of the square class
        Returns:
            area: Square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print('')
