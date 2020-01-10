#!/usr/bin/python3
class Square:
    """This is a class Square defined by size."""
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method of the square class
        Args:
            size (int): Private attribute
            position (int, int): Private attribute of new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Private instance attribute getter method.
        Returns:
            property: Private attribute position
        """
        return(self.__position)

    @position.setter
    def position(self, value):
        """Private instance attribute property setter."""
        if (len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print('')

    def __str__(self):
        """ Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print('')
