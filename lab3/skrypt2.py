from model import MoveDirection
from controller import OptionsParser
import sys
print("start")
def run(moves):
    defs = {
        MoveDirection.forward: 'przód',
        MoveDirection.backward: 'tył',
        MoveDirection.right: 'prawo',
        MoveDirection.left: 'lewo'
    }
    descriptions = [defs[move] for move in moves]
    for arr in descriptions:
        print(arr)
    

if __name__ == "__main__":
    moves = OptionsParser.parse(sys.argv[1:])
    run(moves)

