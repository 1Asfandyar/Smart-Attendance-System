// this will push some testing data to DB
import mongoose from "mongoose";
import "dotenv/config";
import { Department } from "./Schema/Department.js";
import { Section } from "./Schema/Section.js";
import { Teacher } from "./Schema/Teacher.js";
import { Class } from "./Schema/Class.js";
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

  // const dept = new Department({
  //   name: "BCE",
  //   department_id: "BCE",
  //   sections_list: ["A", "B"],
  //   teachers_list: ["TA", "TB"],
  // });

  // await dept.save();
  // const sec = new Section({
  //   name: "A",
  //   section_id: "VIII-A",
  //   department_id: "BCE",
  //   students_list: ["Abdur Rahman", "Abdullah", "Ahmad Zahid"],
  //   students_face_encodings:
  //     "b'AQAAAAAAAAACAAAAAAAAAAMAAAAAAAAABAAAAAAAAAAFAAAAAAAAAAEAAAAAAAAAAgAAAAAAAAADAAAAAAAAAAQAAAAAAAAABQAAAAAAAAA='",
  //   students_names_encodings:
  //     "b'QQAAAGIAAABkAAAAdQAAAHIAAAAgAAAAUgAAAGEAAABoAAAAbQAAAGEAAABuAAAAQQAAAGIAAABkAAAAdQAAAGwAAABsAAAAYQAAAGgAAAAAAAAAAAAAAAAAAAAAAAAAQQAAAGgAAABtAAAAYQAAAGQAAAAgAAAAWgAAAGEAAABoAAAAaQAAAGQAAAAAAAAA'",
  // });
  // await sec.save();
  const t_1 = new Teacher({
    name: "Dr. Habib",
    teacher_id: "habbib",
    department_list: ["BCE"],
    class_list: ["ML-18"],
  });
  const t_2 = new Teacher({
    name: "M. Hafsa",
    teacher_id: "hafsa",
    department_list: ["BCE"],
    class_list: ["DIP-Lab-18"],
  });
  const t_3 = new Teacher({
    name: "Dr. Ahmad",
    teacher_id: "ahmad",
    department_list: ["BCE"],
    class_list: ["DSA-18"],
  });

  const c_1 = new Class({
    subject: "Machine Learning",
    class_id: "ML-18",
    teacher_id: "habbib",
    attendence_id: "A",
    start_time: "9:30",
    end_time: "10:45",
  });

  const c_2 = new Class({
    subject: "Data Structures & Algo",
    class_id: "DSA-18",
    teacher_id: "ahmad",
    attendence_id: "B",
    start_time: "10:50",
    end_time: "11:30",
  });

  const c_3 = new Class({
    subject: "Digital Image Processing Lab",
    class_id: "DIP-Lab-18",
    teacher_id: "hafsa",
    attendence_id: "C",
    start_time: "11:45",
    end_time: "01:30",
  });

  await t_1.save();
  await t_2.save();
  await t_3.save();
  await c_1.save();
  await c_2.save();
  await c_3.save();
  console.log("done");
};

Seed();
