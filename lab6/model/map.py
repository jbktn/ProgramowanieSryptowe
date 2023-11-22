from model.interface import IMoveValidator, IWorldMap
from model.core import Vector2d, MoveDirection
from model.animal import Animal
from view import MapVisualizer

class PositionAlreadyOccupiedError(Exception):
    def __init__(self, position: Vector2d) -> None:
        self.position = position
        print(f"Position {position} is already occupied.")

class WorldMap(IMoveValidator, IWorldMap):
    def move(self, animal: Animal, direction: MoveDirection) -> None:
        if animal.position in self.animals.keys():
            del self.animals[animal.position]
        animal.move(direction,self)
        self.animals[animal.position] = animal

    def isOccupied(self, position: Vector2d) -> bool:
        if position in self.animals.keys():
            return True
        else:
            return False
        
    def place(self, animal: Animal) -> bool:
        if self.canMoveTo(animal.position):
            self.animals[animal.position] = animal
            return True
        else:
            raise PositionAlreadyOccupiedError(animal)
        
    def objectAt(self, position: Vector2d) -> Animal | None:
        if position in self.animals.keys():
            return self.animals[position]
        else:
            return None
        
    def canMoveTo(self, position: Vector2d) -> bool:
        if position in self.animals.keys():
            return False
        else:
            return True

class RectangularMap(WorldMap):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.animals: dict[Vector2d, Animal] = {}

    def __str__(self) -> str:
        map_vizualizer = MapVisualizer(self)
        MapVisualizer.draw(Vector2d(0, 0), Vector2d(self.width, self.height))   

    def canMoveTo(self, position: Vector2d) -> bool:
        if self.width < position.x or self.height < position.y or 0 > position.x or 0 > position.y or position in self.animals.keys():
            return False
        else:
            return True
        

        
class InfiniteMap(WorldMap):
    def __init__(self):
        self.animals: dict[Vector2d, Animal] = {}
    
    def __str__(self):
        top = 0
        bottom = 0
        right = 0
        left = 0
        for animal in self.animals.values():
            top = max(top, animal.position.y)
            bottom = min(bottom, animal.position.y)
            right = max(right, animal.position.x)
            left = min(left, animal.position.x)        
        map_vizualizer = MapVisualizer(self)
        return map_vizualizer.draw(Vector2d(left, bottom), Vector2d(right, top))