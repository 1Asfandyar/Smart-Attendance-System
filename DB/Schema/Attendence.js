import mongoose from "mongoose";
const { Schema } = mongoose;

const attendenceSchema = new Schema({
  attendence_id: {
    type: String,
    required: true,
    unique: true,
    message: "Attendence ID is required",
  },
  time: {
    type: Date,
    required: true,
    message: "Time of attendece is required",
  },
  present_students: [{ type: String, required: true }],
  absent_students: [{ type: String, required: true }],
});

export const Attendence = mongoose.model("Attendence", attendenceSchema);
