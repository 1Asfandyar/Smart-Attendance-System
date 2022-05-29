import { Class } from "../DB/Schema/Class.js";

// this function is passed to filter function
// filter function pass three arguments like func(value, index, array)
// so here value = {start_time, end_time}
const ifClassTime = ({ start_time, end_time }, index, array, max_limit = 1) => {
  // convert "HH:MM" to HH.MM/60
  const s_time =
    parseInt(start_time.split(":")[0]) +
    parseInt(start_time.split(":")[1]) / 60;
  const e_time =
    parseInt(end_time.split(":")[0]) + parseInt(end_time.split(":")[1]) / 60;
  // getting current time
  const current_date = new Date();
  const current_time = current_date.getHours() + current_date.getMinutes() / 60;
  if (current_time >= s_time && current_time < e_time + max_limit) return true;
  else return false;
};

export const getCurrentClass = async (req, res) => {
  const { teacher_id } = req.body;

  let results = await Class.find(
    { teacher_id: teacher_id },
    { student_fcae_encodings: 0, student_names_encodings: 0 }
  );
  results = results.filter(ifClassTime);
  console.log(results);
  res.json(results);
};

export const createNewClass = () => {
  console.log("createNewClass");
};
