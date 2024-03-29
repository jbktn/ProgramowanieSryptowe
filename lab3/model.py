from enum import Enum

class MoveDirection(Enum):
    forward = 1
    backward = 2
    left = 3
    right = 4

class Vector2d:
    def __init__(self, x1, y1):
        self.__x = x1
        self.__y = y1

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.getter
    def x(self):
        return self.__x
    
    @y.getter
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f'({self.__x},{self.__y})'

    def precedes(self, other):
        return self.__x <= other.get_x() and self.__y <= other.get_y()

    def follows(self, other):
        return self.__x >= other.get_x() and self.__y >= other.get_y()

    def add(self, other):
        return Vector2d(self.__x + other.get_x(), self.__y + other.get_y())

    def subtract(self, other):
        return Vector2d(self.__x - other.get_x(), self.__y - other.get_y())

    def upperRight(self, other):
        return Vector2d(max(self.__x, other.get_x()), max(self.__y, other.get_y()))

    def lowerLeft(self, other):
        return Vector2d(min(self.__x, other.get_x()), min(self.__y, other.get_y()))

    def opposite(self):
        return Vector2d(-self.__x, -self.__y)

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

