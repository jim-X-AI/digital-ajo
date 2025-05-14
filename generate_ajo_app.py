import os
from pathlib import Path


def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:  # Added encoding='utf-8'
        f.write(content)


def generate_ajo_app():
    # Create package.json
    package_json = """{
  "name": "digital-ajo",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.14.2",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
"""
    create_file("digital-ajo/package.json", package_json)

    # Create public/index.html
    index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Digital Ajo for your trusted circles" />
    <title>Digital Ajo</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""
    create_file("digital-ajo/public/index.html", index_html)

    # Create src/index.js
    index_js = """import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
"""
    create_file("digital-ajo/src/index.js", index_js)

    # Create src/App.js
    app_js = """import { Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import CreateGroup from './pages/CreateGroup';
import JoinGroup from './pages/JoinGroup';
import GroupDashboard from './pages/GroupDashboard';
import HistoryPage from './pages/HistoryPage';
import './App.css';

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
"""
    create_file("digital-ajo/src/App.js", app_js)

    # Create src/App.css
    app_css = """.app {
  min-height: 100vh;
  background-color: #f5f5f5;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

button {
  cursor: pointer;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  transition: all 0.3s ease;
}

button:hover {
  opacity: 0.9;
  transform: translateY(-2px);
}

input, select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 100%;
  margin-bottom: 15px;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  padding: 20px;
  margin-bottom: 20px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.table th, .table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.table th {
  background-color: #f8f9fa;
  font-weight: bold;
}

.btn-primary {
  background-color: #4CAF50;
  color: white;
}

.btn-secondary {
  background-color: #2196F3;
  color: white;
}

.btn-danger {
  background-color: #f44336;
  color: white;
}

.text-center {
  text-align: center;
}

.mt-3 {
  margin-top: 15px;
}

.mb-3 {
  margin-bottom: 15px;
}
"""
    create_file("digital-ajo/src/App.css", app_css)

    # Create pages
    # LandingPage.js
    landing_page = """import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/LandingPage.css';

function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="landing-container">
      <div className="landing-card">
        <h1 className="logo">Digital Ajo</h1>
        <p className="tagline">Digital Ajo for your trusted circles.</p>

        <div className="button-group">
          <button 
            className="btn-primary"
            onClick={() => navigate('/create-group')}
          >
            Start a New Group
          </button>
          <button 
            className="btn-secondary"
            onClick={() => navigate('/join-group')}
          >
            Join a Group
          </button>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
"""
    create_file("digital-ajo/src/pages/LandingPage.js", landing_page)

    # LandingPage.css
    landing_page_css = """.landing-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #4CAF50, #2196F3);
}

.landing-card {
  background: white;
  padding: 40px;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  max-width: 500px;
  width: 90%;
}

.logo {
  color: #4CAF50;
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.tagline {
  color: #666;
  margin-bottom: 30px;
  font-size: 1.1rem;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.button-group button {
  width: 100%;
  padding: 15px;
  font-size: 1rem;
}
"""
    create_file("digital-ajo/src/styles/LandingPage.css", landing_page_css)

    # CreateGroup.js
    create_group = """import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/CreateGroup.css';

function CreateGroup() {
  const [formData, setFormData] = useState({
    name: '',
    members: '',
    amount: '',
    frequency: 'weekly'
  });
  const [groupCode, setGroupCode] = useState('');
  const [inviteLink, setInviteLink] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real app, this would call an API
    const code = Math.random().toString(36).substring(2, 8).toUpperCase();
    setGroupCode(code);
    setInviteLink(`${window.location.origin}/join-group?code=${code}`);
  };

  return (
    <div className="container">
      <h1>Create Ajo Group</h1>

      {!groupCode ? (
        <form onSubmit={handleSubmit} className="card">
          <label>Group Name</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />

          <label>Member Emails (comma separated)</label>
          <input
            type="text"
            name="members"
            value={formData.members}
            onChange={handleChange}
            placeholder="email1@example.com, email2@example.com"
            required
          />

          <label>Contribution Amount</label>
          <input
            type="number"
            name="amount"
            value={formData.amount}
            onChange={handleChange}
            required
          />

          <label>Frequency</label>
          <select
            name="frequency"
            value={formData.frequency}
            onChange={handleChange}
            required
          >
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="monthly">Monthly</option>
          </select>

          <button type="submit" className="btn-primary">
            Create Group
          </button>
        </form>
      ) : (
        <div className="card">
          <h2>Group Created Successfully!</h2>
          <p><strong>Group Code:</strong> {groupCode}</p>
          <p><strong>Invite Link:</strong> 
            <a href={inviteLink} target="_blank" rel="noopener noreferrer">
              {inviteLink}
            </a>
          </p>
          <button 
            className="btn-secondary mt-3"
            onClick={() => navigate(`/group/${groupCode}`)}
          >
            Go to Group Dashboard
          </button>
        </div>
      )}
    </div>
  );
}

export default CreateGroup;
"""
    create_file("digital-ajo/src/pages/CreateGroup.js", create_group)

    # CreateGroup.css
    create_group_css = """.container h1 {
  margin-bottom: 20px;
  color: #333;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}
"""
    create_file("digital-ajo/src/styles/CreateGroup.css", create_group_css)

    # JoinGroup.js
    join_group = """import React, { useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import '../styles/JoinGroup.css';

function JoinGroup() {
  const [groupCode, setGroupCode] = useState('');
  const [name, setName] = useState('');
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  React.useEffect(() => {
    const code = searchParams.get('code');
    if (code) {
      setGroupCode(code);
    }
  }, [searchParams]);

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate(`/group/${groupCode}`);
  };

  return (
    <div className="container">
      <h1>Join Ajo Group</h1>

      <form onSubmit={handleSubmit} className="card">
        <label>Group Code</label>
        <input
          type="text"
          value={groupCode}
          onChange={(e) => setGroupCode(e.target.value)}
          required
        />

        <label>Your Name (Optional)</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="This helps identify you in the group"
        />

        <button type="submit" className="btn-primary">
          Join Group
        </button>
      </form>
    </div>
  );
}

export default JoinGroup;
"""
    create_file("digital-ajo/src/pages/JoinGroup.js", join_group)

    # GroupDashboard.js
    group_dashboard = """import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import '../styles/GroupDashboard.css';

function GroupDashboard() {
  const { id } = useParams();
  const [file, setFile] = useState(null);

  // Mock data - in a real app, this would come from an API
  const group = {
    name: "Family Ajo",
    amount: "NGN 20,000",  // Changed from ₦ to NGN to avoid encoding issues
    frequency: "Weekly",
    nextPayout: "2023-06-15",
    members: [
      { id: 1, name: "Aisha", paid: true, received: true, proof: "receipt1.jpg" },
      { id: 2, name: "Tunde", paid: true, received: false, proof: "receipt2.jpg" },
      { id: 3, name: "Chukwuemeka", paid: false, received: false, proof: null },
    ],
    nextToReceive: "Tunde"
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    // In a real app, you would upload this file to a server
  };

  return (
    <div className="container">
      <div className="header">
        <h1>{group.name}</h1>
        <Link to={`/group/${id}/history`} className="btn-secondary">
          View History
        </Link>
      </div>

      <div className="card">
        <h2>Group Details</h2>
        <p><strong>Amount:</strong> {group.amount}</p>
        <p><strong>Frequency:</strong> {group.frequency}</p>
        <p><strong>Next Payout:</strong> {group.nextPayout}</p>
      </div>

      <div className="card">
        <h2>Member Status</h2>
        <table className="table">
          <thead>
            <tr>
              <th>Member</th>
              <th>Paid?</th>
              <th>Received?</th>
              <th>Proof</th>
            </tr>
          </thead>
          <tbody>
            {group.members.map(member => (
              <tr key={member.id}>
                <td>{member.name}</td>
                <td>{member.paid ? 'Yes' : 'No'}</td>
                <td>{member.received ? 'Yes' : 'No'}</td>
                <td>
                  {member.proof ? (
                    <a href={`/proofs/${member.proof}`} target="_blank" rel="noopener noreferrer">
                      [View]
                    </a>
                  ) : (
                    <label className="upload-label">
                      [Upload]
                      <input 
                        type="file" 
                        style={{ display: 'none' }} 
                        onChange={handleFileChange}
                      />
                    </label>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="card">
        <h2>Next to Receive</h2>
        <p>{group.nextToReceive} is next to receive the payout.</p>
      </div>
    </div>
  );
}

export default GroupDashboard;
"""
    create_file("digital-ajo/src/pages/GroupDashboard.js", group_dashboard)

    # GroupDashboard.css
    group_dashboard_css = """.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.upload-label {
  color: #2196F3;
  cursor: pointer;
  text-decoration: underline;
}

.upload-label:hover {
  color: #0d8bf2;
}
"""
    create_file("digital-ajo/src/styles/GroupDashboard.css", group_dashboard_css)

    # HistoryPage.js
    history_page = """import React from 'react';
import { useParams } from 'react-router-dom';
import '../styles/HistoryPage.css';

function HistoryPage() {
  const { id } = useParams();

  // Mock data - in a real app, this would come from an API
  const history = [
    { date: "2023-05-01", recipient: "Aisha", proofs: ["proof1.jpg", "proof2.jpg"] },
    { date: "2023-04-15", recipient: "Chukwuemeka", proofs: ["proof3.jpg"] },
    { date: "2023-04-01", recipient: "Tunde", proofs: ["proof4.jpg"] },
  ];

  return (
    <div className="container">
      <h1>Group History</h1>

      <div className="card">
        <table className="table">
          <thead>
            <tr>
              <th>Date</th>
              <th>Payout Recipient</th>
              <th>Payment Proofs</th>
            </tr>
          </thead>
          <tbody>
            {history.map((item, index) => (
              <tr key={index}>
                <td>{item.date}</td>
                <td>{item.recipient}</td>
                <td>
                  {item.proofs.map((proof, i) => (
                    <span key={i}>
                      <a href={`/proofs/${proof}`} target="_blank" rel="noopener noreferrer">
                        [Proof {i+1}]
                      </a>{' '}
                    </span>
                  ))}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default HistoryPage;
"""
    create_file("digital-ajo/src/pages/HistoryPage.js", history_page)

    print("Digital Ajo React application generated successfully!")
    print("Navigate to the 'digital-ajo' directory and run:")
    print("1. npm install")
    print("2. npm start")


if __name__ == "__main__":
    generate_ajo_app()