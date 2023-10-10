import sys

def display(args,show_index): 
    if show_index is True:
        for arg, i in args:
            print(f'args[{i}] = {arg}')
    else:
        for arg in args:
            print(f'{arg}')


if __name__ == "__main__":
    arr = list(sys.argv[0:])
    index=False
    print("System wystartował.")
    display(arr, index)
    print("System zakończył działanie.")