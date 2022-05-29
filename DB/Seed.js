// this will push some testing data to DB
import mongoose from "mongoose";
import "dotenv/config";
import { Department } from "./Schema/Department.js";
const { MONGODB_LINK } = process.env;

const Seed = async () => {
  // handling the Database link
  try {
    await mongoose.connect(MONGODB_LINK);
    console.log("Connected to Database");
  } catch (error) {
    console.log("ERROR in conneting to Database");
    console.log(error);
    return;
  }

  const dept = new Department({
    department_id: "BCE",
    sections_list: ["A", "B"],
    teachers_list: ["TA", "TB"],
  });

  dept.show();
};

Seed();
