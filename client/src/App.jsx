import "./App.css";

import { Routes, Route } from "react-router-dom";

import Login from "./Components/Login";
import DashBoard from "./Components/DashBoard";
import Error from "./Components/Error";
import Profile from "./Components/Profile";
import { AuthProvider } from "./Components/utils/auth";

function App() {
  return (
    <>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/dashboard" element={<DashBoard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="*" element={<Error />} />
        </Routes>
      </AuthProvider>
    </>
  );
}

export default App;
