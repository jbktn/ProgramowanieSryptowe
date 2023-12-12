class Room {
    constructor(number, limit, price, guests) {
        this.number = number;
        this.limit = limit;
        this.price = price;
        this.guests = guests;
    }
    print_room = () => {
        console.group(`Room number: ${this.number}`);
        console.log(`Limit: ${this.limit}`);
        console.log(`Price: ${this.price}`);
        console.log(`Guests: ${this.guests}`);
        console.groupEnd();
    }
}

class Resevation {
    constructor(guest, room, arrival, departure, price) {
        this.guest = guest;
        this.room = room;
        this.arrival = arrival;
        this.departure = departure;
        this.price = price;
    }
}

const rooms = [new Room(1, 1, 100, []), new Room(2, 3, 300, []), new Room(3, 2, 200, [])]

let reservations = []           

hotel =  () => {
    let commands = document.getElementById('command_console').value;
    commands = commands.split(" ");
                  
    switch (commands[0].toLowerCase()) {
        case 'book':
            book(commands.slice(1));
            break;
        case 'guests':
            guests();
            break;
        case 'guest':
            guest(commands.slice(1));
            break;
        case 'hotel':
            hotel_print();
            break;
        default:
            console.warn('Invalid command');
            break;
    }
    document.getElementById('command_console').value = '';
}

book = (params) => {
    const number = parseInt(params[0]);
    const name = params[1];
    const surname = params[2];
    const arrival = new Date(params[3]);
    const departure = new Date(params[4]);

    const room = rooms.find(room => room.number === number);
    console.group('book');
    if (room) {
        if (room.guests.length < room.limit) {                                                            
            console.log('Room Number:', number);
            console.log('Guest Name:', name + " " + surname);
            console.log('Arrival:', arrival);
            console.log('Departure:', departure);                                                            
            room.guests.push(`${name} ${surname}`);
            var time_diff = departure.getTime() - arrival.getTime();
            var days_past = time_diff / (1000 * 60 * 60 * 24);
            var price = days_past * room.price;
            console.log(`Price: ${price}`);
            reservations.push(new Resevation(name + " " + surname, room, arrival, departure, price))                               
        } else {
            console.error('Room is full');
        }
    } else {
        console.warn('Room not found');
    }
    console.groupEnd();
}

guests = () => {
    console.group('guests');
    let guestlist = []
    for (const room of rooms) {
        guestlist = [...guestlist, ...room.guests]
    }
    guestlist = [...new Set(guestlist)];
    console.log(guestlist);
    console.groupEnd();
}

guest = (params) => {
    const name = params[0];
    const surname = params[1];
    console.group('guest: ', `${name} ${surname}`);
    for (const room of rooms) {
        if (room.guests.includes(`${name} ${surname}`)) {                              
            console.log(`Room ${room.number} is rented by ${name} ${surname}`);
        }
    }
    var to_pay = 0;
    for (const reservation of reservations) {
        if (reservation.guest === `${name} ${surname}`) {
            to_pay = to_pay + parseInt(reservation.price);
        }
    }
    console.log(`To pay: ${to_pay}`)
    console.groupEnd(); 
}

hotel_print = () => {
    console.group('hotel');
    for (const room of rooms) {
        room.print_room();
    }
    console.groupEnd();
}

