import sys
import json

with open("file_name", "r") as file:
    data = json.load(file)

def add(person, room_nr):
    for room in data:
        if room["number"] == room_nr:
            if len(room["guests"]) < room["limit"]:
                room["guests"].append(person)
                print("operacja_udana")
            print("pokoj_pelny")


def clear():
    for room in data:
        room["guests"] = []
    with open("file_name", "w") as file:
        json.dump(data, file, indent=4)


def print_rooms():
    print("-------------+--------+\nNumer pokoju |\
 Goście |\n-------------+--------+")
    for room in data:
        print(f"{room['number']}", end="")
        for i in range(1, room["limit"] + 1):
            if i == 1:
                print("",end="")
            else:
                print(" ",end="")
            print(f"              {i}. ",end="")
            try:
                print(f"{json.dumps(room['guests'][i - 1], indent = 4, sort_keys=True)}")
            except IndexError:
                print("")
        print('')

if __name__ == "__main__":
    file_name = sys.argv[1]

    lines = sys.stdin.read()
    for line in lines:
        