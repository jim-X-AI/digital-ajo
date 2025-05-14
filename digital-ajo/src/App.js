import { Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import CreateGroup from './pages/CreateGroup';
import JoinGroup from './pages/JoinGroup';
import GroupDashboard from './pages/GroupDashboard';
import HistoryPage from './pages/HistoryPage';
import './App.css';
import './index.css';

function App() {
  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/create-group" element={<CreateGroup />} />
        <Route path="/join-group" element={<JoinGroup />} />
        <Route path="/group/:id" element={<GroupDashboard />} />
        <Route path="/group/:id/history" element={<HistoryPage />} />
      </Routes>
    </div>
  );
}

export default App;
