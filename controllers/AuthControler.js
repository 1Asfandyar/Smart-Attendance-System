export const logInController = (req, res) => {
  console.log("login Controller");
};

export const logOutController = (req, res) => {
  console.log(req.body);
  console.log("Logout Controller");
};
