import mongoose from "mongoose";
const { Schema } = mongoose;

const departmentSchema = new Schema({
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
    required: true,
    message: "Attendence ID is required",
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
});

export const Department = mongoose.model("Department", departmentSchema);
