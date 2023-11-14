from model.core import MoveDirection, Vector2d, MapDirection
from model.animal import Animal
from model.map import RectangularMap
from view import MapVisualizer
from time import sleep
import sys

class OptionsParser:
    def parse(args):
        directions = []
        for arg in args:
            try:
                directions.append(MoveDirection(arg))
            except ValueError:
                continue
        return directions
    
class Simulation:
    animals = []
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d], map: RectangularMap) -> None:
        self.directions = directions
        self.positions = positions
        self.map = map
        for position in positions:
            self.map.place(Animal(position))
            self.animals.append(Animal(position))

    def run(self):
        print(self.map)
        for i in range(len(self.directions)):
            self.map.move(self.animals[i%len(self.animals)],self.directions[i])
            sleep(0.25)
            print(self.map) 