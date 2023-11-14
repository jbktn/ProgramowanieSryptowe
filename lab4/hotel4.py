import datetime

class Room:
    def __init__(self, number: int, current: int, max: int, cena: int) -> None:
        self.number = number
        self.current = current
        self.cena = cena
        self.max = max

    def __repr__ (self):
        return f"Numer: {self.number} Ilosc miejsc: {self.max} Ilosc miejsc zajętych: {self.current} Cena: {self.cena} "

    def __str__(self):
        return f"Numer: {self.number} Ilosc miejsc: {self.max} Ilosc miejsc zajętych: {self.current} Cena: {self.cena} "

    
class Guest:
    reservations = []
    def __init__(self, pesel, name, surname):
        self.pesel = pesel
        self.name = name
        self.surname = surname
            
    def __repr__(self):
        return f"{self.pesel} {self.name} {self.surname}"

    def __str__(self):
        return f"{self.pesel} {self.name} {self.surname}"

class Reservation:
    def __init__(self, guest, room, check_inDate, check_outDate):
        self.guest:Guest = guest
        self.room:Room = room
        self.check_inDate: datetime.date = check_inDate
        self.check_outDate: datetime.date = check_outDate

    def __repr__(self):
        cena = (self.check_outDate - self.check_inDate).days * self.room.cena
        return f"{self.guest} {self.room} {self.check_inDate} {self.check_outDate} Do zaplaty: {cena} zł\n"

    def __str__(self):
        cena = (self.check_outDate - self.check_inDate).days * self.room.cena
        return f"{self.check_inDate} {self.check_outDate} Do zaplaty: {cena} zł\n"
    
class Hotel:
    rooms = []
    def __init__(self) -> None:
        self.reservations: list[Reservation] = []

    def book(self, room_nr, pesel, arrival, departure):
        is_room = False
        for room in self.rooms:
            if room.number == int(room_nr):
                is_room = True
                if room.current >= room.max:
                    print("Room in full")
                    return
                the_room = room
        if is_room == False:
            print("Room not known")
            numer = input("Insert room id munber: ")
            max = input("Insert room guest limit: ")
            cena = input("Inser room price per day: ")
            self.rooms.append(Room(numer, 0, cena, max))
        is_pesel = False
        for reservation in self.reservations:
            if reservation.guest.pesel == pesel:
                the_guest = reservation.guest
                is_pesel = True
        if is_pesel == False:
            print("Guest not known, add Guest")
            name = input("Insert Name: ")
            surname = input("Inser Surname: ")
            the_guest = Guest(pesel, name, surname)
        self.reservations.append(Reservation(the_guest, the_room, arrival, departure))
        the_room.current += 1
                
    def pesel_check(self, pesel):
        for reservation in self.reservations:
            if reservation.guest.pesel == pesel:
                return True
        return False
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        self.rooms.append(reservation.room)

    def print_room(self, number):
        for room in self.rooms:
            if room.number == number:
                print(room)
                for reservation in self.reservations:
                    if reservation.room.number == number:
                        print(reservation)

    def print_guests(self):
        for reservation in self.reservations:
            return reservation.guest

    def print_guest(self, pesel):
        for reservation in self.reservations:
            if reservation.guest.pesel == pesel:
                print(f"{reservation.guest}\n")
                print(reservation)

    def search_range(self, date_1, date_2):
        reservations_in_range = []

        for reservation in self.reservations:
            if date_1 <= reservation.check_outDate and date_2 >= reservation.check_inDate:
                reservations_in_range.append(reservation)

        if not reservations_in_range:
            print("Brak rezerwacji w podanym zakresie dat")
            return

        print(f"Rezerwacje w zakresie dat {date_1} - {date_2}:")
        for reservation in reservations_in_range:
            cena = (reservation.check_outDate - reservation.check_inDate).days * reservation.room.cena
            print(f"Termin: {reservation.check_inDate} - {reservation.check_outDate}, Numer pokoju: {reservation.room.number}, Kwota do zapłaty: {cena} zł")

if __name__ == "__main__":
    hotel = Hotel()
    hotel.add_reservation(
        Reservation(
            Guest("7", "Maciej", "Musiał"),
            Room(1, 0, 0, 300),
            datetime.datetime(2000, 1, 1),
            datetime.datetime(2000, 1, 2)))
    hotel.add_reservation(
        Reservation(
            Guest("12", "Tomasz", "Kot"),
            Room(2, 0, 1, 150),
            datetime.datetime(2000, 1, 1),
            datetime.datetime(2000, 1, 5)))
    hotel.add_reservation(
        Reservation(
            Guest("22", "Katarzyna", "Szlak"),
            Room(3, 0, 2, 100),
            datetime.datetime(2000, 1, 1),
            datetime.datetime(2000, 1, 10)))

    while True:
        try:
            try:
                line = input()
                commands = line.split(" ")
                if commands[0] == "rooms":
                    print(hotel.rooms)
                elif commands[0] == "room":
                    hotel.print_room(int(commands[1]))
                elif commands[0] == "guests":
                    print(hotel.reservations)
                elif commands[0] == "guest":
                    try:
                        hotel.print_guest(commands[1])
                    except IndexError:
                        print("No such guest")
                elif commands[0] == "book":
                    hotel.book(commands[1], int(commands[2]), datetime.datetime.strptime(commands[3], "%Y-%m-%d"), datetime.datetime.strptime(commands[4], "%Y-%m-%d"))
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