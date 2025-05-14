import React, { useState } from 'react';
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
