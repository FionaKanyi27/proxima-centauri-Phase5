import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function GroupCreate({ token }) {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/api/groups', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ name, description }),
    });
    if (response.ok) {
      navigate('/dashboard');
    } else {
      alert('Failed to create group');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-2xl mb-4">Create Group</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Group Name" className="w-full p-2 mb-4 border rounded" required />
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" className="w-full p-2 mb-4 border rounded"></textarea>
        <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded">Create</button>
      </form>
    </div>
  );
}

export default GroupCreate;