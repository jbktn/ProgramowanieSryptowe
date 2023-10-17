def cut(input_text, dlimit, position):

    lines = input_text.splitlines()
    for line in lines:
        string = line.split(dlimit)
        string = string[position - 1]
        print(string)
