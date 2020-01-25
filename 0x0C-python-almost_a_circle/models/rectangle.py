#!/usr/bin/python3
"""
Rectangle

"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        if self.__width == 0 or self.__height == 0:
            print('')
        else:
            for i in range(self.__y):
                print('')
            for i in range(self.__height):
                for k in range(self.__x):
                    print(' ', end='')
                for j in range(self.__width):
                    print('#', end='')
                print('')

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            i = 0
            att_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        dic = {}
        i = 0
        att_list = ['id', 'width', 'height', 'x', 'y']
        for k, v in self.__dict__.items():
            if hasattr(self, k):
                dic.update({att_list[i]: v})
            i += 1
        return dic
