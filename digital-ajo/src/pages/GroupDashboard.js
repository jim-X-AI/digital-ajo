import React, { useState } from 'react';
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
