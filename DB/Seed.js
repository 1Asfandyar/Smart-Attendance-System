// this will push some testing data to DB
import mongoose from "mongoose";
import "dotenv/config";
import { Department } from "./Schema/Department.js";
import { Section } from "./Schema/Section.js";
const { MONGODB_LINK } = process.env;

const Seed = async () => {
  // handling the Database link
  let con;
  try {
    con = await mongoose.connect(MONGODB_LINK);
    console.log("Connected to Database");
  } catch (error) {
    console.log("ERROR in conneting to Database");
    console.log(error);
    return;
  }

  const dept = new Department({
    name: "BCE",
    department_id: "BCE",
    sections_list: ["A", "B"],
    teachers_list: ["TA", "TB"],
  });

  await dept.save();
  const sec = new Section({
    name: "A",
    section_id: "VIII-A",
    department_id: "BCE",
    students_list: ["Abdur Rahman", "Abdullah", "Ahmad Zahid"],
    students_face_encodings:
      "b'AQAAAAAAAAACAAAAAAAAAAMAAAAAAAAABAAAAAAAAAAFAAAAAAAAAAEAAAAAAAAAAgAAAAAAAAADAAAAAAAAAAQAAAAAAAAABQAAAAAAAAA='",
    students_names_encodings:
      "b'QQAAAGIAAABkAAAAdQAAAHIAAAAgAAAAUgAAAGEAAABoAAAAbQAAAGEAAABuAAAAQQAAAGIAAABkAAAAdQAAAGwAAABsAAAAYQAAAGgAAAAAAAAAAAAAAAAAAAAAAAAAQQAAAGgAAABtAAAAYQAAAGQAAAAgAAAAWgAAAGEAAABoAAAAaQAAAGQAAAAAAAAA'",
  });
  await sec.save();
  console.log("done");
};

Seed();
