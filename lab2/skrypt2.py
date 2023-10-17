import sys

pipe_positions = []

for i in range(len(sys.argv[1:])):
    if sys.argv[i] == "|":
        pipe_positions.append(i)

input = sys.argv[1:]

if sys.argv[1] == "grep":
    import grep
    word = False
    case = False
    
    for i in range(1, len(input)):
        if input[i] == "-i":
            case = True
        elif input[i] == "-w":
            word = True
        else:
            phrase = input[i]
    lines = sys.stdin.read()
    grep.grep(phrase, lines, case, word)

elif sys.argv[1] == "cut":
    import cut
    dlimit = " "
    for i in range(1, len(input), 2):
        if input[i] == "-d":
            dlimit = input[i + 1]
        elif input[i] == "-f":
            position = int(input[i + 1])
    lines = sys.stdin.read()
    
    cut.cut(lines, dlimit, position)