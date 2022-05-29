import express from "express";
import {
  getCurrentClass,
  createNewClass,
} from "../controllers/ClassController.js";

const router = express.Router();

router.get("/", getCurrentClass);
router.post("/", createNewClass);

export default router;
