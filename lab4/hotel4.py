import datetime



class Room:
    guests_str = ""
    def __init__(self, number, cena, max: int, current: int, guests) -> None:
        self.number = number
        self.cena = cena
        self.max = max
        self.current = current
        self.guests = guests

    def __repr__ (self):
        return f"nr: {self.number} Aktualna liczba gosci: {self.current}"

    def __str__(self):
        return f"Numer: {self.number}\nMaksymalna liczba osób: {self.max}\nAktualna liczba osób: {len(self.guests)}\nCena: {self.cena}"\
if self.current == 0 else f"Numer: {self.number}\nMaksymalna liczba osób: {self.max}\nAktualna liczba osób: {len(self.guests)}\n\
Cena: {self.cena}\nGoście:\n{self.guests_str}"
    
class Hotel:
    list_of_rooms = [
    Room(1, 100, 1, 0, []),
    Room(2, 200, 2, 0, []),
    Room(3, 300, 3, 0, [])
    ]
    def __init__(self, rooms: list_of_rooms) -> None:
        self.rooms = rooms

class Guest:
    reservations = []
    def __init__(self, name):
        self.name = name

    def book(self, room, arrival, departure):
        if room.current < room.max:
            room.guests_str += f"   {self.name} {arrival} {departure}\n"
            cena = (departure - arrival).days * room.cena
            self.reservations.append({"room":room.number, "from":arrival, "to":departure, "price":cena})
            room.current += 1
        else:
            print("Err. Room is full")
            
    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        data = f"Imię: {self.name}\n"
        for i in self.reservations:
            data += f"Pokoj nr: {i['room']}   {i['from']}    {i['to']}\nDo zaplaty: {i['price']} zł\n"
        return data



list_of_guests = [Guest("Jan Kowalski"), Guest("Anna Kowalska"), Guest("Joanna Bielecka")] 

'''room = list_of_rooms[0]
guest = list_of_guests[2]
guest.book(room, datetime.date(2024, 1, 1), datetime.date(2024, 1, 3))
guest = list_of_guests[0]
guest.book(room, datetime.date(2024, 1, 1), datetime.date(2024, 1, 3))
print(list_of_guests[0]) '''

if __name__ == "__main__":
    while True:
        try:
            try:
                line = input()
                commands = line.split(" ")
                if commands[0] == "rooms":
                    print(list_of_rooms)
                elif commands[0] == "guests":
                    print(list_of_guests)
                elif commands[0] == "guest":
                    print(list_of_guests[int(commands[1])])
                elif commands[0] == "book":
                    list_of_guests[int(commands[1])].book(list_of_rooms[int(commands[2])], datetime.datetime.strptime(commands[3], "%d-%m-%Y"), datetime.datetime.strptime(commands[4], "%d-%m-%Y"))
                else:
                    print("Nieznana komenda")
            except IndexError:
                print("Niepoprawny format komendy")
        except EOFError:
            quit()