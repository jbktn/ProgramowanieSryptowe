from model import MoveDirection

class OptionsParser:
    def parse(args):
        valid_directions = {'f', 'b', 'l', 'r'}
        directions = []
        for arg in args:
            if arg in valid_directions:
                if arg == 'f':
                    directions.append(MoveDirection.forward)
                elif arg == 'b':
                    directions.append(MoveDirection.backward)
                elif arg == 'l':
                    directions.append(MoveDirection.left)
                elif arg == 'r':
                    directions.append(MoveDirection.right)
        return directions