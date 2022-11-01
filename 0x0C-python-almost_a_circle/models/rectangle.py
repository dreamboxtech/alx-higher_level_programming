#!/usr/bin/python3
"""
A simple rectangle file

"""
from base import Base


class Rectangle(Base):
    """This implements a rectanlge
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """The default constructor for the base class
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Sets it as attribute and not a method"""
        return self.__width

    @width.setter
    def width(self, value):
        """This check for constriants and sets the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Sets it as attribute and not a method"""
        return self.__height

    @height.setter
    def height(self, value):
        """This check for constriants and sets the value"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")

        if value <= 0:
            raise ValueError("height be > 0")
        self.__height = value

    @property
    def x(self):
        """Sets it as attribute and not a method"""
        return self.__x

    @x.setter
    def x(self, value):
        """This check for constriants and sets the value"""
        if not isinstance(value, int):
            raise TypeError("x must be >= 0")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Sets it as attribute and not a method"""
        return self.__y

    @y.setter
    def y(self, value):
        """This check for constriants and sets the value"""
        if not isinstance(value, int):
            raise TypeError("y must be >= 0")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """simply returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle woth and #"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args):
        """Updates the rectangle """
        # args[0] = self.id
        # args[1] = self.__width
        # args[2] = self.__height
        # args[3] = self.__x
        # args[4] = self.__y
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v




    def __str__(self):
        """A string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/" +\
            f"{self.__y} - {self.__width}/{self.__height}"










