from typing import Self
from enum import Enum

class MoveDirection(Enum):
    FORWARD = 'f'
    BACKWARD = 'b'
    LEFT = 'l'
    RIGHT = 'r'

class Vector2d:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)
    
    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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
        next_direction = {
            MapDirection.NORTH: MapDirection.EAST,
            MapDirection.SOUTH: MapDirection.WEST,
            MapDirection.WEST: MapDirection.NORTH,
            MapDirection.EAST: MapDirection.SOUTH
        }
        return next_direction[self]

    def previous(self):
        previous_direction = {
            MapDirection.NORTH: MapDirection.WEST,
            MapDirection.SOUTH: MapDirection.EAST,
            MapDirection.WEST: MapDirection.SOUTH,
            MapDirection.EAST: MapDirection.NORTH
        }
        return previous_direction[self]

    def toUnitVector(self):
        unit_vectors = {
            MapDirection.NORTH: Vector2d(0, 1),
            MapDirection.SOUTH: Vector2d(0, -1),
            MapDirection.WEST: Vector2d(-1, 0),
            MapDirection.EAST: Vector2d(1, 0)
        }
        return unit_vectors[self]

