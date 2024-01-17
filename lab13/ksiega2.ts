import { Application, Router, send } from "https://deno.land/x/oak/mod.ts";
import logger from "https://deno.land/x/oak_logger/mod.ts";
import {
  dejsEngine,
  oakAdapter,
  viewEngine,
} from "https://deno.land/x/view_engine/mod.ts";
import { MongoClient } from "https://deno.land/x/mongo@v0.32.0/mod.ts";

const MONGO_URL: string = Deno.env.get("MONGO_URL") || "mongodb://127.0.0.1:27017";

const app: Application = new Application();
const router: Router = new Router();

app.use(logger.logger);
app.use(logger.responseTime);

app.use(viewEngine(oakAdapter, dejsEngine, { viewRoot: "./views" }));

router.get("/", async (ctx) => {
  await ctx.render("ksiega2.ejs", {
    data: { title: "Forum" },
  });
});

router.get('/data', async function (ctx) {
    try {
        const client = new MongoClient();
        await client.connect(MONGO_URL);
        console.log("Connected correctly to server");
        const db = client.database("FORUM");
        const col = db.collection("wpisy");
        const data = await col.find().toArray();
        console.log(data);
        ctx.response.body = data;
        client.close();
    } catch (err) {
        console.trace(err);
    }
});

router.post('/submit', async function (ctx) {
    try {
        const body = await ctx.request.body().value;
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
        ctx.response.redirect("/");  
    } catch (err) {
        console.trace(err);
    }  
});

app.use(router.routes());
app.use(router.allowedMethods());

console.log("App is listening to port: 8000");
await app.listen({ port: 8000 });