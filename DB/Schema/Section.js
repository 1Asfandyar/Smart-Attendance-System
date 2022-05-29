import mongoose from "mongoose";
const { Schema } = mongoose;

const sectionSchema = new Schema({
  name: {
    type: String,
    unique: true,
    required: true,
    message: "Name of the Section is required",
  },
  section_id: {
    type: String,
    unique: true,
    required: true,
    message: "Department ID of the department is required",
  },
  department_id: {
    type: String,
    required: true,
    message: "Department ID of for section is required",
  },
  students_list: [
    {
      type: String,
      required: true,
      message: "List of Students of the Section is required",
    },
  ],
  students_face_encodings: {
    type: String,
    required: true,
    message: "Face encodings of Students of the Section is required",
  },
  students_names_encodings: {
    type: String,
    required: true,
    message: "Names encodings of Students of the Section is required",
  },
});

export const Section = mongoose.model("Section", sectionSchema);
