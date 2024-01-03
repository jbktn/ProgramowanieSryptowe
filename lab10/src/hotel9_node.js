import http from 'node:http';
import { URL } from 'node:url';
import fs from 'fs/promises';

const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, GET',
    'Access-Control-Max-Age': 2592000,};

async function requestListener(req, res) {
    console.log('--------------------------------------');
    console.log(`The relative URL of the current request: ${req.url}`);
    console.log(`Access method: ${req.method}`);
    console.log('--------------------------------------');

    const url = new URL(req.url, `http://${req.headers.host}`);
    let rooms = [];

    console.log(url);

    let getFile = async (path, fileType) => {
        try {
            let data = await fs.readFile(path);
            res.writeHead(200, {'Content-Type': `${fileType}`,'Content-Length':data.length});
            res.write(data);
            res.end();
        } catch (err) {
            res.writeHead(500, {'Content-Type': 'text/plain'});
            res.write('Internal Server Error');                    
            res.end();

            console.log(err);
        }
    }

    switch ([req.method, url.pathname].join(' ')) {
        case 'GET /':
            getFile('src/hotel9.html', 'text/html');
            break;

        case 'GET /src/hotel9.js':
            getFile('src/hotel9.js', 'text/javascript');
            break;

        case "GET /public/rooms":
            try {
                rooms = await fs.readFile('public/rooms.json', 'utf-8');
                rooms = JSON.parse(rooms);
            } catch (err) {
                console.log(err);
            }
            res.writeHead(200, { ...headers, 'Content-Type': 'application/json'});
            res.write(JSON.stringify(rooms));            
            res.end();
            break;

         case "GET /public/reservations":
            try {
                rooms = await fs.readFile('public/reservations.json', 'utf-8');
                rooms = JSON.parse(rooms);
            } catch (err) {
                console.log(err);
            }
            res.writeHead(200, { ...headers, 'Content-Type': 'application/json'});
            res.write(JSON.stringify(rooms));            
            res.end();
            break;
        
        case 'GET /public/1.jpg':
            getFile('public/images/1.jpg', 'image/jpeg');
            break;

        case 'GET /public/2.jpg':
            getFile('public/images/2.jpg', 'image/jpeg');
            break;

        case 'GET /public/3.jpg':
            getFile('public/images/3.jpg', 'image/jpeg');
            break;

            case 'POST /book':
                console.log('POST');
                var body = '';
                req.on('data', chunk => {
                    body += chunk.toString();
                });
                req.on('end', async () => {
                    body = JSON.parse(body);
                    console.log(body);
                    res.writeHead(200, { ...headers, 'Content-Type': 'application/json'});
                    res.end();
                    let rooms = await fs.readFile('public/rooms.json', 'utf-8');
                    rooms = JSON.parse(rooms);
                    const room = rooms.find(room => {console.log(body.number, room.number); return room.number === body.number})
                    room.guests.push(`${body.name} ${body.surname}`);
                    let newguests = room.guests;
                    let newroom = {number: room.number, guests: newguests, limit: room.limit, price: room.price};
                    const index = rooms.indexOf(room);
                    rooms[index] = newroom;
                    const reservation = {number: room.number, guest: `${body.name} ${body.surname}`, arrival: body.arrival, departure: body.departure, price: body.price};
                    fs.writeFile('public/rooms.json', JSON.stringify(rooms), err => {
                        if (err) throw err;
                    });

                    let reservations = await fs.readFile('public/reservations.json', 'utf-8');
                    reservations = JSON.parse(reservations);
                    reservations.push(reservation);
                    fs.writeFile('public/reservations.json', JSON.stringify(reservations), err => {
                        if (err) throw err;
                    });
                });
                break;
      
        default:
            res.writeHead(501, { 'Content-Type': 'text/plain; charset=utf-8' });
            res.write('Error 501: Not implemented');
            res.end();
    }
}

const server = http.createServer(requestListener);
server.listen(8000);
console.log('The server was started on port 8000');
console.log('To stop the server, press "CTRL + C"');