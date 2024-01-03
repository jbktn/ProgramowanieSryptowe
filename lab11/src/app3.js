import express from 'express';
import morgan from 'morgan';
import { MongoClient } from 'mongodb';

const app = express();

app.set('view engine', 'pug');
app.use(express.static('static'));

app.locals.pretty = app.get('env') === 'development';

app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

app.use('/static', express.static('./static'));

let user = { description: 'User', authorised: true };

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

app.get('/', (request, response) => {
    user = { description: 'User', authorised: false };
    response.render('index', {students, user});
});

app.get('/:wydzial', async (req, res) => {
    const wydzial = req.params.wydzial;
    console.log(wydzial);

    try{
        const client = new MongoClient('mongodb://127.0.0.1:27017');
        await client.connect();
        console.log('Connected successfully to server');

        const db = client.db('AGH');
        const collection = db.collection('students');
        const studentsDB = await collection.find({ 'wydział': wydzial }).toArray();

        console.log(studentsDB);

        res.render('index', {students: studentsDB, user, wydzial});

        client.close();
    } catch (error) {
        console.log(error);
    }
});

app.listen(8000, () => {
    console.log('The server was started on port 8000');
    console.log('To stop the server, press "CTRL + C"');
});          