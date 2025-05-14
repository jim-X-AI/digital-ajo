import os
from pathlib import Path


def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def fix_ajo_app():
    # Create missing index.css
    index_css = """/* Basic reset and styles */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
"""
    create_file("digital-ajo/src/index.css", index_css)

    # Create missing HistoryPage.css
    history_page_css = """/* Add any specific styles for HistoryPage here */
.history-table {
  width: 100%;
}

.history-table a {
  margin-right: 10px;
}
"""
    create_file("digital-ajo/src/styles/HistoryPage.css", history_page_css)

    # Create missing JoinGroup.css
    join_group_css = """/* Add any specific styles for JoinGroup here */
.join-form {
  max-width: 500px;
  margin: 0 auto;
}
"""
    create_file("digital-ajo/src/styles/JoinGroup.css", join_group_css)

    # Fix GroupDashboard.js
    group_dashboard_js = """import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import '../styles/GroupDashboard.css';

function GroupDashboard() {
  const { id } = useParams();

  // Mock data - in a real app, this would come from an API
  const group = {
    name: "Family Ajo",
    amount: "NGN 20,000",
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
    // In a real app, you would upload this file to a server
    console.log("File selected:", e.target.files[0]);
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
    create_file("digital-ajo/src/pages/GroupDashboard.js", group_dashboard_js)

    # Fix HistoryPage.js
    history_page_js = """import React from 'react';
import { useParams } from 'react-router-dom';
import '../styles/HistoryPage.css';

function HistoryPage() {
  const { id } = useParams();
  console.log("Group ID:", id); // Now using the id parameter

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
        <table className="table history-table">
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
    create_file("digital-ajo/src/pages/HistoryPage.js", history_page_js)

    # Fix App.js to ensure correct import case
    app_js = """import { Routes, Route } from 'react-router-dom';
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
"""
    create_file("digital-ajo/src/App.js", app_js)

    print("All fixes applied successfully!")
    print("1. Created missing CSS files")
    print("2. Fixed unused variables in components")
    print("3. Ensured proper case sensitivity in imports")
    print("4. Added index.css import to App.js")
    print("\nNow you can run:")
    print("cd digital-ajo && npm start")


if __name__ == "__main__":
    fix_ajo_app()