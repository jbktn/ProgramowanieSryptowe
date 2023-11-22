import datetime

class Room:
    def __init__(self, number: int, current: int, max: int, cena: int) -> None:
        self.number = number
        self.cena = cena
        self.max = max

    def current(self, numer):
        exit = 0
        for guest, reservations in hotel.guests.items():
            for reservation in reservations:
                if reservation.room is Room and reservation.room.number == self.number:
                    exit += 1
        return exit

    def __repr__ (self):
        return f"Numer: {self.number} Ilosc miejsc: {self.max} Ilosc miejsc zajętych: {self.current(self.number)} Cena: {self.cena} "

    def __str__(self):
        return f"Numer: {self.number} Ilosc miejsc: {self.max} Ilosc miejsc zajętych: {self.current(self.number)} Cena: {self.cena} "

class ConferenceRoom:
    def __init__(self, number, max, cena, wyposazenie) -> None:
        self.number = number
        self.max = max
        self.cena = cena
        self.wyposazenie = wyposazenie

    def current(self, numer):
        exit = 0
        for reservations in self.guests.items():
            for reservation in reservations:
                if reservation.room is ConferenceRoom and reservation.room.number == self.number:
                    exit += 1
        return exit
    
    def __repr__(self) -> str:
        return f"{self.number}"
    
    def __str__(self) -> str:
        return f"{self.number} Ilosc miejsc zajętych: {self.current(self.number)} {self.max} {self.cena} {self.wyposazenie}"
        
class Guest:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
            
    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def __hash__(self):
        return hash((self.name, self.surname))
    
    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

class Reservation:
    def __init__(self, room, check_inDate, check_outDate):
        self.room = room
        self.check_inDate: datetime.date = check_inDate
        self.check_outDate: datetime.date = check_outDate

    def __repr__(self):
        cena = int((self.check_outDate - self.check_inDate).days * self.room.cena)
        if self.room.__class__.__name__ == "Room":          
            return f"Room: {self.room.number} {self.check_inDate} {self.check_outDate} Do zaplaty: {cena} zł\n"
        elif self.room.__class__.__name__ == "ConferenceRoom":
            cena = cena * 24
            return f"ConferenceRoom: {self.room.number} {self.check_inDate} {self.check_outDate} Do zaplaty: {cena} zł\n"

    def __str__(self):
        cena = int((self.check_outDate - self.check_inDate).days * self.room.cena)
        if self.room.__class__.__name__ == "Room":
            return f"Room: {self.room.number} {self.check_inDate} {self.check_outDate} Do zaplaty: {cena} zł\n"
        elif self.room.__class__.__name__ == "ConferenceRoom":
            cena = cena * 24
            return f"ConferenceRoom: {self.room.number} {self.check_inDate} {self.check_outDate} Do zaplaty: {cena} zł\n"
    
class Hotel:
    rooms = []
    ConferenceRooms = []
    def __init__(self) -> None:
        self.guests: [Guest, list[Reservation]] = {}

    def book(self, id, number, name, surname, arrival, departure):
        is_room = False
        if id == "room":
            for room in self.rooms:
                if room.number == int(number):
                    is_room = True
                    if Room.current(number) >= room.max:
                        print("Room in full")
                        return
                    target = room
            if is_room == False:
                print("Room not known")
                max = input("Insert room guest limit: ")
                cena = input("Inser room price per day: ")
                target = Room(number, 0, cena, max)
                self.rooms.append(target)
        elif id == "ConferenceRoom":
            for ConRoom in self.ConferenceRooms:
                if ConRoom.number == int(number):
                    is_room = True
                    if ConferenceRoom.current(number) >= ConRoom.max:
                        print("Room in full")
                        return
                    target = ConRoom
            if is_room == False:
                print("ConferenceRoom not known")
                max = input("Insert room guest limit: ")
                cena = input("Inser room price per hour: ")
                target = ConferenceRoom(number, 0, cena, max)
                self.ConferenceRooms.append(target)

        guest = Guest(name, surname)
        if guest not in self.guests.keys():
            print("Guest not known, adding Guest")
            self.guests[Guest(name, surname)] = [Reservation(target, arrival, departure)]
            return
        else:
            self.guests[guest].append(Reservation(target, arrival, departure))
    
    def add_reservation(self, name, surname, reservation):
        guest = Guest(name, surname)
        self.rooms.append(reservation.room)
        if guest in self.guests:
            self.guests[guest].append(reservation)
        else:
            self.guests[Guest(name, surname)] = [reservation]

    def print_room(self, number):
        for room in self.rooms:
            if room.number == number:
                print(room)
        for guest, reservations in self.guests.items():
            for reservation in reservations:
                if reservation.room.number == number:
                    print(guest)
                    print(reservation)

    def print_ConferenceRoom(self, number):
        for room in self.ConferenceRooms:
            if room.number == number:
                print(room)
        for guest, reservations in self.guests.items():
            for reservation in reservations:
                if reservation.room.number == number:
                    print(guest)
                    print(reservation)

    def print_guest(self, name, surname):
        guest = Guest(name, surname)
        print(guest)
        print(self.guests[guest])

    def search_range(self, start_date, end_date):
        reservations_in_range = []

        for guest, reservations in self.guests.items():
            for reservation in reservations:
                if reservation.check_inDate <= end_date and reservation.check_outDate >= start_date:
                    reservations_in_range.append((guest, reservation))

        if not reservations_in_range:
            print("Brak rezerwacji w podanym zakresie dat")
            return

        print(f"Rezerwacje w zakresie dat {start_date} - {end_date}:")
        for guest, reservation in reservations_in_range:
            print(f"Gość: {guest.imie} {guest.nazwisko}, Nr pokoju: {reservation.room.numer}, Data: {reservation.check_inDate} - {reservation.check_outDate}")

if __name__ == "__main__":
    hotel = Hotel()
    hotel.add_reservation(
        "Maciej", "Musiał",
        Reservation(Room(1, 0, 0, 300), datetime.datetime(2000, 1, 1), datetime.datetime(2000, 1, 2)))
    hotel.add_reservation(
        "Tomasz", "Kot",
        Reservation(Room(2, 0, 1, 150), datetime.datetime(2000, 1, 1), datetime.datetime(2000, 1, 5)))
    hotel.add_reservation(
        "Katarzyna", "Szlak",
        Reservation(Room(3, 0, 2, 100), datetime.datetime(2000, 1, 1), datetime.datetime(2000, 1, 10)))

    while True:
        try:
            try:
                line = input()
                commands = line.split(" ")
                if commands[0] == "rooms":
                    print(hotel.rooms)
                elif commands[0] == "room":
                    hotel.print_room(int(commands[1]))
                elif commands[0] == "ConferenceRooms":
                    print(hotel.ConferenceRooms)
                elif commands[0] == "ConferenceRoom":
                    hotel.print_ConferenceRoom(int(commands[1]))
                elif commands[0] == "test":
                    print(hotel.guests)
                elif commands[0] == "guests":
                    for guest in hotel.guests.keys():
                        print(guest)
                elif commands[0] == "guest":
                    try:
                        hotel.print_guest(commands[1], commands[2])
                    except IndexError:
                        print("No such guest")
                elif commands[0] == "book":
                    if commands[1] == "room":
                        hotel.book('room', commands[2], commands[3], commands[4], datetime.datetime.strptime(commands[5], "%Y-%m-%d"), datetime.datetime.strptime(commands[6], "%Y-%m-%d"))
                    elif commands[1] == 'ConferenceRoom':
                        hotel.book('ConferenceRoom', commands[2], commands[3], commands[4], datetime.datetime.strptime(commands[5], "%Y-%m-%d"), datetime.datetime.strptime(commands[6], "%Y-%m-%d"))
                elif commands[0] == "range":
                    hotel.search_range(datetime.datetime.strptime(commands[1], "%Y-%m-%d"), datetime.datetime.strptime(commands[2], "%Y-%m-%d"))
                elif commands[0] == "exit":
                    quit()
                else:
                    print("Nieznana komenda")
            except IndexError:
                print("Niepoprawny format komendy")
        except EOFError:
            quit()