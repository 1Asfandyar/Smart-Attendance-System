import mongoose from "mongoose";
const { Schema } = mongoose;

const departmentSchema = new Schema({
  name: {
    type: String,
    unique: true,
    required: true,
    message: "Name of the department is required",
  },
  department_id: {
    type: String,
    unique: true,
    required: true,
    message: "Department ID of the department is required",
  },
  sections_list: [
    {
      type: String,
      required: true,
      message: "List of Sections of the department is required",
    },
  ],
  teachers_list: [
    {
      type: String,
      required: true,
      message: "List of Teachers of the department is required",
    },
  ],
});

export const Department = mongoose.model("Department", departmentSchema);
