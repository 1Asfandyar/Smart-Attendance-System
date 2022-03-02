import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Auth from "./Pages/Auth";
import DashBoard from "./Pages/DashBoard";
import ErrorPage from "./Pages/ErrorPage";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Auth />} />
          <Route path="/dashboard" element={<DashBoard />} />
          <Route path="/*" element={<ErrorPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
