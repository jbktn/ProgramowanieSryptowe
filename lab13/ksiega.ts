import express, { Express, Request, Response } from "npm:express@^4";
import { MongoClient } from "https://deno.land/x/mongo@v0.32.0/mod.ts";

const MONGO_URL: string = Deno.env.get("MONGO_URL") || "mongodb://127.0.0.1:27017";

const app: Express = express();
const port: number = 8000;
app.use(express.json());

app.get('/ksiega.html', function (_req: Request, res: Response) {
    res.send(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Forum</title>
                <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet'>
            </head>
            <body>
                <main>
                    <div>
                        <h1>Forum</h1>
                    </div>
                    <div id="posts-container"></div>
                    <p class="title">Nowy wpis:</p>
                    <form id="post-form">
                        <div class="form-group">               
                            <label for="id">Twoje imię i nazwisko</label>
                            <input type="text" class="form-control" id="id" placeholder="Jerzy Wiśniewski">
                        </div>
                        <div class="form-group">
                            <label for="content">Treść wpisu</label>
                            <textarea class="form-control" id="content" rows="3" placeholder="Proszę o kontakt osoby, które ze mną studiowały — tel. 12 345 67 89 "></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" onclick='window.location.reload();'>Dodaj wpis</button>
                    </form>         
                </main>
                <style>
                    body {
                        font-family: 'Roboto';
                        font-size: .9375rem;
                        font-weight: 400;
                        line-height: 1.5;
                        color: #1d2125;
                        text-align: left;
                    }
                    .form-control {
                        display: block;
                        width: 60vw;
                        height: calc(1.5em + 0.75rem + 2px);
                        padding: .375rem .75rem;
                        line-height: 1.5;
                        color: #495057;
                        background-color: #fff;
                        background-clip: padding-box;
                        border: 1px solid #8f959e;
                        border-radius: .5rem;
                        transition: border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;
                    }
                    .form-group {
                        margin-bottom: 1rem;
                    }
                    label {
                        display: inline-block;
                        margin-bottom: .5rem;
                    }
                    .title {
                        display: block;
                        width: 100%;
                        max-width: 100%;
                        padding: 0;
                        margin-bottom: 0.5rem;
                        font-size: 1.5rem;
                        line-height: inherit;
                        color: inherit;
                        white-space: normal;
                    }
                    .btn {
                        display: inline-block;
                        font-weight: 400;
                        text-align: center;
                        vertical-align: middle;
                        user-select: none;
                        border: 1px solid transparent;
                        padding: .375rem .75rem;
                        font-size: .9375rem;
                        line-height: 1.5;
                        border-radius: .5rem;
                        transition: color 0.15s ease-in-out,background-color 0.15s ease-in-out,border-color 0.15s ease-in-out,box-shadow 0.15s ease-in-out;
                        cursor: pointer;
                        border-radius: 8px;
                    }
                    .btn-primary {
                        margin-top: 1rem;
                        color: #fff;
                        background-color: #393743;
                        border-color: #393743;
                    }
                </style>
                <script lang="ts">
                    const renderPosts = (posts) => {
                        const root = document.querySelector('#posts-container');
                        for (let post of posts) {
                            var div = document.createElement('div');
                            div.style.backgroundColor = '#a7a1a0';
                            div.style.borderRadius = '8px';
                            div.style.margin = '1rem';

                            var h2 = document.createElement('h2');
                            h2.innerText = post.id;
                            h2.style.padding = '0.5rem';
                            h2.style.margin = '0';

                            var p = document.createElement('p');
                            p.innerText = post.content;
                            p.style.padding = '0.5rem';
                            p.style.margin = '0';

                            div.appendChild(h2);
                            div.appendChild(p);
                            root.appendChild(div);
                        }
                    };

                    addEventListener('load', function() {
                        fetch('/data', {method: 'GET'})
                            .then(response => response.json())
                            .then(data => {var wpisy = data; renderPosts(wpisy);})
                            .catch(err => console.trace(err));
                    });
                    
                    document.querySelector('#post-form').addEventListener('submit', function(event) {
                        event.preventDefault();
                        let id = document.querySelector('#id').value;
                        let content = document.querySelector('#content').value;
                        let post = {id: id, content: content};
                        fetch('/submit', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(post)})
                    });
                </script>
            </body>
            </html>`);
        });

app.get('/', function (_req: Request, res: Response) {
    res.redirect('/ksiega');
});

app.get('/data', async function (req: Request, res: Response) {
    const client = new MongoClient();
    await client.connect(MONGO_URL);
    console.log("Connected correctly to server");
    const db = client.database("FORUM");
    const col = db.collection("wpisy");
    const data = await col.find().toArray();
    console.log(data);
    res.json(data);
    client.close();
});

app.post('/submit', async function (req: Request, res: Response) {
    try {
        const body = req.body;
        const id: string = body.id;
        const content: string = body.content;

        const client = new MongoClient();
        await client.connect(MONGO_URL);
        console.log("Connected correctly to server");
        const db = client.database("FORUM");
        const col = db.collection("wpisy");
        const data = await col.insertOne({ id, content });
        console.log(data);
        client.close();
        res.redirect("/");  
    } catch (err) {
        console.trace(err);
    }  
});

app.listen(port, function () {
    console.log('The application is available on port 8000');
});