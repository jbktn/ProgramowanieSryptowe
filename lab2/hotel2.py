import sys
import json

def add(person, room_nr, time):
    for room in data:
        if room["number"] == room_nr:
            if len(room["guests"]) < room["limit"]:
                room["guests"].append(person)
                room["terminy"].append(time)


def clear():
    for room in data:
        room["guests"] = []
        room["terminy"] = []
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def print_rooms():
    print("-------------+--------+--------+\n\
Numer pokoju | Goście | Termin |\n\
-------------+--------+--------+")
    for room in data:
        print(f"{room['number']}", end="")
        for i in range(1, room["limit"] + 1):
            if i == 1:
                print("",end="")
            else:
                print(" ",end="")
            print(f"             {i}. ",end="")
            try:
                print(f"{json.dumps(room['guests'][i - 1], indent = 4, sort_keys=True)}    {json.dumps(room['terminy'][i - 1], indent = 4, sort_keys=True)}")
            except IndexError:
                print("")
        print('')

def show(person):
    print(person)
    print("---------------------+------------\n\
Termin               | Numer pokoju\n\
---------------------+------------")
    for room in data:
        for i in range(room["limit"]):
            try:
                if room["guests"][i] == person:
                    print(f"{room["terminy"][i]}  {room["number"]}")
            except IndexError:
                None
    print("\n")

if __name__ == "__main__":
    file_name = sys.argv[1]

    with open(file_name, "r") as file:
        data = json.load(file)

    while True:
        try:
            try:
                line = input()
                commands = line.split(" ")
                if commands[0] == "rooms":
                    print_rooms()
                elif commands[0] == "show":
                    commands.pop(0)
                    commands = commands[0].split(",")
                    for person in commands:
                       show(person)
                elif commands[0] == "book":
                    commands.pop(0)
                    for arr in commands:    
                        comm = arr.split("|")
                        person = comm[0]
                        times = comm[1]
                        times = times.split(":")
                        for arr in times:
                            info = arr.split("(")
                            time = info[0]
                            room = info[1]
                            room_nr = int(room.split(")")[0])
                            if 1 <= room_nr <= 3:
                                add(person, room_nr, time)
                            else:
                                print(f"Pokój numer {room_nr} nie istnieje")
                elif commands[0] == "clear":
                    clear()
                else:
                    print("Nieznana komenda")
            except IndexError:
                print("Niepoprawny format komendy")
        except EOFError:
            quit()

        