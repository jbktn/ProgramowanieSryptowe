def first_character(string):
    return string[0]

def first_two_characters(string):
    if len(string) > 1:
        return string[0:2]
    return ""
    
def all_characters_except_first_two(string):
    return string[2:]

def penultimate_character(string):
    if len(string) > 2:
        return string[-2]
    return ""

def last_three_characters(string):
    if len(string) > 2:
        return string[-3:]
    return ""
    
def all_characters_in_even_positions(string):
    return string[::2]

def merge_characters_and_duplicate(string):
    out = first_character(string) + penultimate_character(string)
    return out * len(string)