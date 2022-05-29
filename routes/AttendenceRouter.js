import express from "express";
import {
  getCurrentClassStatus,
  saveClassAttendence,
} from "../controllers/AttendenceController.js";

const router = express.Router();

router.get("/", getCurrentClassStatus);
router.post("/", saveClassAttendence);

export default router;
