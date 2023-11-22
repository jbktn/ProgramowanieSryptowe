from model.core import MoveDirection, Vector2d, MapDirection
from model.animal import Animal
from model.map import RectangularMap, PositionAlreadyOccupiedError
from view import MapVisualizer
from time import sleep
import sys

class OptionsParser:
    @staticmethod 
    def parse(args):
        directions = list(filter(lambda x: x in ['f','r','b','l'], args))
        return [MoveDirection(directions.index(x)+1) for x in directions]
    
class Simulation:
    animals = []
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d], map: RectangularMap) -> None:
        self.directions = directions
        self.positions = positions
        self.map = map
        for position in positions:
            try:
                self.map.place(Animal(position))
            except: PositionAlreadyOccupiedError
            self.animals.append(Animal(position))

    def run(self):
        sleep(1)
        print(self.map)
        for i in range(len(self.directions)):
            self.map.move(self.animals[i%len(self.animals)],self.directions[i])
            sleep(1)
            print(self.map) 