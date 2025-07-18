import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function GroupDetails({ token }) {
  const [group, setGroup] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const fetchGroup = async () => {
      const response = await fetch(`http://localhost:5000/api/groups/${id}`, {
        headers: { 'Authorization': `Bearer ${token}` },
      });
      if (response.ok) {
        const data = await response.json();
        setGroup(data);
      }
    };
    fetchGroup();
  }, [id, token]);

  if (!group) return <div>Loading...</div>;

  return (
    <div className="max-w-4xl mx-auto mt-10 p-6 bg-white rounded shadow">
      <h2 className="text-2xl mb-4">{group.name}</h2>
      <p className="mb-4">{group.description}</p>
      <h3 className="text-xl mb-2">Members</h3>
      <ul>
        {group.members.map(member => (
          <li key={member.id} className="p-2 border-b">{member.email} ({member.role})</li>
        ))}
      </ul>
    </div>
  );
}

export default GroupDetails;