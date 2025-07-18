import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';

function Dashboard({ token }) {
  const [groups, setGroups] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchGroups = async () => {
      const response = await fetch('http://localhost:5000/api/groups', {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setGroups(data);
      } else {
        navigate('/');
      }
    };
    fetchGroups();
  }, [token, navigate]);

  return (
    <div className="max-w-4xl mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-2xl mb-4">Dashboard</h2>
      <Link to="/groups/create" className="p-2 bg-blue-500 text-white rounded mb-4 inline-block">Create Group</Link>
      <Link to="/transactions" className="p-2 bg-green-500 text-white rounded mb-4 inline-block ml-4">Make Transaction</Link>
      <h3 className="text-xl mb-2">Your Groups</h3>
      <ul>
        {groups.map(group => (
          <li key={group.id} className="p-2 border-b">
            <Link to={`/groups/${group.id}`} className="text-blue-500">{group.name}</Link> - {group.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;