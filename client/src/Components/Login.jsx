import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./utils/auth";

function Login() {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");

  const auth = useAuth();
  const navigate = useNavigate();

  const handleUserChange = (e) => {
    setUserName(e.target.value);
  };

  const handlePassChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = () => {
    console.log(`User Name: ${userName}`);
    console.log(`Password: ${password}`);

    // if success
    auth.login(userName);
    // redirect to dashboard
    navigate("/dashboard", { replace: true });
  };

  return (
    <div>
      <h2>Login</h2>
      User Name: <input type="text" onChange={handleUserChange} />
      Password <input type="password" onChange={handlePassChange} />
      <button type="submit" onClick={handleSubmit}>
        Login
      </button>
    </div>
  );
}

export default Login;
