export const getCurrentClass = (req, res) => {
  console.log("getCurrentClass");
  console.log(req.body);
  res.send("getCurrentClass");
};

export const createNewClass = () => {
  console.log("createNewClass");
};
