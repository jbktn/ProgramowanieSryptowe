from model import MoveDirection, Vector2d, Animal, MapDirection
import sys

class OptionsParser:
    def parse(args):
        valid_directions = {'f', 'b', 'l', 'r'}
        directions = []
        for arg in args:
            if arg in valid_directions:
                if arg == 'f':
                    directions.append(MoveDirection.FORWARD)
                elif arg == 'b':
                    directions.append(MoveDirection.BACKWARD)
                elif arg == 'l':
                    directions.append(MoveDirection.LEFT)
                elif arg == 'r':
                    directions.append(MoveDirection.RIGHT)
        return directions
    
class Simulation:
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d]) -> None:
        self.directions = directions
        self.animals = [Animal(position) for position in positions]

    def run(self):
        for i in range(len(self.directions)):
            animal_nr = i % len(self.animals)
            direction = self.directions[i]
            animal = self.animals[animal_nr]
            print(f"Zwierze {animal_nr} : {animal.position} {animal.orientation}")
            animal.move(direction)