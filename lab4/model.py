from typing import Self
from enum import Enum

class MoveDirection(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

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

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
            return f'{self.position} {self.orientation}'
        
    def __repr__(self) -> str:
        return str(self)
    
    def isAt(self, position: Vector2d) -> bool:
        return self.position == position
    
    def inMAP(self, position) -> bool:
        return 0 <= position.x <= 4 and 0 <= position.y <= 4

    def move(self, direction: MoveDirection) -> None:
        if direction == MoveDirection.RIGHT:
            self.orientation = self.orientation.next()
            new_position = self.position
        elif direction == MoveDirection.LEFT:
            self.orientation = self.orientation.previous()
            new_position = self.position
        elif direction == MoveDirection.FORWARD:
            new_position = self.position + self.orientation.toUnitVector()
        elif direction == MoveDirection.BACKWARD:
            new_position = self.position - self.orientation.toUnitVector()

        if self.inMAP(new_position):
            self.position = new_position
