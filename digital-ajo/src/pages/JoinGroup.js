import React, { useState } from 'react';
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
