import express from "express";
import bodyParser from "body-parser";
import mongoose from "mongoose";
import "dotenv/config";

import AuthRouter from "./routes/AuthRouter.js";
import ClassRouter from "./routes/ClassRouter.js";
import AttendenceRouter from "./routes/AttendenceRouter.js";

const PORT = process.env.PORT || 3000;
const { MONGODB_LINK } = process.env;

const app = express();

app.use("/", express.static("./client/dist/index.html"));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use("/api/auth", AuthRouter);
app.use("/api/class", ClassRouter);
app.use("/api/attendence", AttendenceRouter);

const start = async () => {
  // handling the Database link
  try {
    await mongoose.connect(MONGODB_LINK);
    console.log("Connected to Database");
  } catch (error) {
    console.log("ERROR in conneting to Database");
    console.log(error);
    return;
  }

  // starting the server
  try {
    app.listen(PORT, () => console.log(`Running at PORT:${PORT}`));
  } catch (error) {
    console.log("ERROR in starting the server");
    console.log(error);
    return;
  }
};

start();
