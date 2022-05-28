import express from "express";
import {
  logInController,
  logOutController,
} from "../controllers/AuthControler.js";

const router = express.Router();

router.get("/", logInController);
router.post("/", logOutController);

export default router;
