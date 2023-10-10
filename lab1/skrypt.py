import sys

def display(args,show_index): 
    if show_index is True:
        for arg, i in args:
            print(f'args[{i}] = {arg}')
    else:
        for arg in args:
            print(f'{arg}')

def run(moves, move_descriptions):
    for i in range(len(moves)):
        moves[i] = move_descriptions[moves[i]]
    display(moves, False)

move_descriptions = {
        "f": "Zwierzak idzie do przodu",
        "b": "Zwierzak idzie do tyłu",
        "l": "Zwierzak skręca w lewo",
        "r": "Zwierzak skręca w prawo"
    }
    
if __name__ == "__main__":
    args = list(sys.argv[1:])
    print("System wystartował.")
    display(args, False)
    run(args, move_descriptions)
    print("System zakończył działanie.")