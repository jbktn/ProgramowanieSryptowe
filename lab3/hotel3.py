class Room:
    def __init__(self):
        self.room_number = 1
        self.room_capacity = 3
        self.room_price = 200

        self.current_occupancy = 0
        self.guests = {}

    def check_in(self, guest_name, checkin_date, checkout_date):
        if self.current_occupancy < self.room_capacity:
            self.current_occupancy += 1
            self.guests[guest_name] = {'checkin_date': checkin_date, 'checkout_date': checkout_date}
            print(f"{guest_name} zameldowany. Aktualna liczba osób: {self.current_occupancy}")
        else:
            print("Pokój pełny. Nie można dokonać zameldowania.")

    def check_out(self, guest_name):
        if guest_name in self.guests:
            self.current_occupancy -= 1
            checkout_date = self.guests[guest_name]['checkout_date']
            print(f"{guest_name} wymeldowany. Data wymeldowania: {checkout_date}. Aktualna liczba osób: {self.current_occupancy}")
            del self.guests[guest_name]
        else:
            print(f"{guest_name} nie jest zameldowany w pokoju.")

'''
if __name__ == "__main__":
    # Tworzenie instancji klasy Room
    room_instance = Room()

    # Wyświetlanie informacji o pokoju
    print(f"Numer pokoju: {room_instance.room_number}")
    print(f"Limit osób w pokoju: {room_instance.room_capacity}")
    print(f"Aktualna liczba osób: {room_instance.current_occupancy}")
    print(f"Cena pokoju: {room_instance.room_price}")

    # Przykłady zameldowania i wymeldowania gości
    room_instance.check_in("Gość1", "2023-10-25", "2023-10-28")
    room_instance.check_in("Gość2", "2023-10-26", "2023-10-29")
    room_instance.check_in("Gość3", "2023-10-27", "2023-10-30")

    room_instance.check_out("Gość2")
'''

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
                    print(list_of_guests[commands[1]])
                elif commands[0] == "book":
                    list_of_guests[commands[1]].book(list_of_rooms[commands[2]], datetime.strptime(commands[3],str), datetime.strptime(commands[4],str))
                elif commands[0] == "clear":
                    clear()
                else:
                    print("Nieznana komenda")
            except IndexError:
                print("Niepoprawny format komendy")
        except EOFError:
            quit()