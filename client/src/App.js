import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Auth from "./Pages/Auth";
import DashBoard from "./Pages/DashBoard";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Auth />} />
          <Route path="/dashboard" element={<DashBoard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
