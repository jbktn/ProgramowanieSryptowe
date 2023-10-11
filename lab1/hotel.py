import sys

stan_pokoi = {
    "1": [' ', ' '],

    "2": [' ', ' ', ' '],
    "3": [' ', ' ']
}

limity = {
    "1": 1,
    "2": 3,
    "3": 2
}


def rez(osoba, pokoj):
    pok = stan_pokoi[pokoj]
    for i in range(limity[pokoj]):
        if stan_pokoi[pokoj][i] == ' ':
            stan_pokoi[pokoj][i] = osoba
        



if __name__ == "__main__":
    input = sys.argv[1:]
    for i in range(len(input)):
        if input[i] != "--stan_pokoi":
            rez(input[i], input[i + 1])
            i += 1
        elif input[i] == "--stan_pokoi":
            print(f"-------------+--------+\nNumer pokoju | Goście |\n-------------+--------+\n\
1           1.{stan_pokoi['1'][0]}\n\n\
2           1.{stan_pokoi['2'][0]}\n\
            2.{stan_pokoi['2'][1]}\n\
            3.{stan_pokoi['2'][2]}\n\n\
3           1.{stan_pokoi['3'][0]}\n\
            2.{stan_pokoi['3'][1]}\n\
")
            
