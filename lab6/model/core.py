from typing import Self
from enum import Enum

class MoveDirection(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class Vector2d:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def log(funkcja):
        def wrapper(*args, **kwargs):
            print(f'Nazwa kwalifikowana: Vector2d:{funkcja.__name__}')
            print(f"Argumenty: ", end="")
            for arg in args:
                print(f'{arg} ', end="")
            print('',end='\n')
            return funkcja(*args, **kwargs)
        return wrapper
    
    def log_to(file):
        def decorator(funkcja):
            def wrapper(*args, **kwargs):
                args_str = ' '.join([str(arg) for arg in args])
                wpis = f"Vector2d.{funkcja.__name__} | {args_str}"

                with open(file, 'a') as log_file:
                    log_file.write(wpis + '\n')
               
                return funkcja(*args, **kwargs)
            return wrapper
        return decorator
    
    @property
    @log_to('dziennik')
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @log_to('dziennik')
    def add(self, other):
        return Vector2d(self.__x + other.x, self.__y + other.y)
    
    def __str__(self):
        return f'({self.__x},{self.__y})'
    
    def __repr__(self):
        return f'({self.__x},{self.__y})'
       
    def __add__(self, other):
        return Vector2d(self.__x + other.x, self.__y + other.y)

    def __sub__(self, other):
        return Vector2d(self.__x - other.x, self.__y - other.y)
    
    def __hash__(self):
        return hash(self.__x)

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

class MapDirection(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def __str__(self):
        direction_str = {
            MapDirection.NORTH: '↑',
            MapDirection.SOUTH: '↓',
            MapDirection.WEST: '←',
            MapDirection.EAST: '→'
        }
        return direction_str[self]

    def next(self):
        if self == MapDirection.NORTH:
            return MapDirection.EAST
        elif self == MapDirection.EAST:
            return MapDirection.SOUTH
        elif self == MapDirection.SOUTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.NORTH

    def previous(self):
        if self == MapDirection.NORTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.SOUTH
        elif self == MapDirection.SOUTH:
            return MapDirection.EAST
        elif self == MapDirection.EAST:
            return MapDirection.NORTH

    def toUnitVector(self):
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)

