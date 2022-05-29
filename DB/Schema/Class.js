import mongoose from "mongoose";
const { Schema } = mongoose;

const classSchema = new Schema({
  subject: {
    type: String,
    unique: true,
    required: true,
    message: "Subject of the department is required",
  },
  class_id: {
    type: String,
    unique: true,
    required: true,
    message: "Class ID is required",
  },
  teacher_id: {
    type: String,
    unique: true,
    required: true,
    message: "Teacher ID is required",
  },
  attendence_id: {
    type: String,
  },
  start_time: {
    type: String,
    required: true,
    message: "Starting time of the Class is requied.",
  },
  end_time: {
    type: String,
    required: true,
    message: "Starting time of the Class is requied.",
  },
  enrolled_students: [{ type: String, required: true, unique: true }],
  student_fcae_encodings: {
    type: String,
    required: true,
    message: "Face base64 encodings is requied.",
  },
  student_names_encodings: {
    type: String,
    required: true,
    message: "Student name encodings is requied.",
  },
});

export const Class = mongoose.model("Class", classSchema);
