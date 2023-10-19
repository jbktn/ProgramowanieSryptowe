import sys
import operations

def ops(x):
    print(operations.first_character(x))
    print(operations.first_two_characters(x))
    print(operations.all_characters_except_first_two(x))
    print(operations.penultimate_character(x))
    print(operations.last_three_characters(x))
    print(operations.all_characters_in_even_positions(x))
    print(operations.merge_characters_and_duplicate(x))

if __name__ == "__main__":
    ops(sys.argv[1])
