import express from "express";
import bodyParser from "body-parser";
import "dotenv/config";

import AuthRouter from "./routes/AuthRouter.js";

const PORT = process.env.PORT || 3000;

const app = express();

app.use("/", express.static("./client/dist/index.html"));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use("/api/auth", AuthRouter);

app.listen(PORT, () => console.log(`Running at PORT:${PORT}`));
