import "./App.css";

import { Routes, Route } from "react-router-dom";

import Login from "./Components/Login";
import DashBoard from "./Components/DashBoard";
import Error from "./Components/Error";
import Profile from "./Components/Profile";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<DashBoard />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="*" element={<Error />} />
    </Routes>
  );
}

export default App;
