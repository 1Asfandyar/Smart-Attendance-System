import mongoose from "mongoose";
const { Schema } = mongoose;

const teacherSchema = new Schema({
  name: {
    type: String,
    required: true,
    message: "Name of the teacher is required",
  },
  teacher_id: {
    type: String,
    unique: true,
    required: true,
    message: "teacher_id is required",
  },
  department_list: [
    {
      type: String,
      message: "List of Sections of the department is required",
    },
  ],
  class_list: [
    {
      type: String,
      required: true,
      message: "List of class of the teacher is required",
    },
  ],
});

export const Teacher = mongoose.model("Teacher", teacherSchema);
