import re

def grep(phrase, input_lines, case, word):
    lines = input_lines.splitlines()

    if case == True & word == True:
        for line in lines:
            if re.search(r'\b'+phrase+r'\b', line, re.IGNORECASE):
                print(line)
    elif word == True:
        for line in lines:
            if re.search(r'\b'+phrase+r'\b', line):
                print(line)
    elif case == True:
        for line in lines:
            if re.search(phrase, line, re.IGNORECASE):
                print(line)
    else:
        for line in lines:
            if re.search(phrase, line):
                print(line)