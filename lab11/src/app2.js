import express from 'express';
import morgan from 'morgan';

/* *************************** */
/* Configuring the application */
/* *************************** */
const app = express();

app.set('view engine', 'pug');
app.use(express.static('static'));

app.locals.pretty = app.get('env') === 'development'; // The resulting HTML code will be indented in the development environment

/* ************************************************ */

app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

app.use('/static', express.static('./static'));

let students = [
    {
          fname: 'Jan',
          lname: 'Kowalski'
    },
    {
          fname: 'Anna',
          lname: 'Nowak'
    },
];

/* ******** */
/* "Routes" */
/* ******** */

/* ------------- */
/* Route 'GET /' */
/* ------------- */
app.get('/', (request, response) => {
    response.render('index', {students}); // Render the 'index' view
});

app.get('/submit', (request, response) => {
    response.send(`Hello ${request.query.name}`); // Send a response with the name from the query string')
});

app.post('/', (request, response) => {
    response.send(`Hello ${request.body.name}`); // Send a response with the name from the request body
});

/* ************************************************ */

app.listen(8000, () => {
    console.log('The server was started on port 8000');
    console.log('To stop the server, press "CTRL + C"');
});          