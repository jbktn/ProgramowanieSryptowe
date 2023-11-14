from model.core import Vector2d, MapDirection, MoveDirection
from model.interface import IMoveValidator

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return str(self.orientation)
        
    def __repr__(self) -> str:
        return str(self.orientation)
    
    def isAt(self,position):
        return position == self.position

    def move(self, direction: MoveDirection, validator: IMoveValidator):
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

        if validator.canMoveTo(new_position):
            self.position = new_position
