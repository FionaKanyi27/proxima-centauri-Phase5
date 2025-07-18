import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import Dashboard from './components/Dashboard';
import GroupCreate from './components/GroupCreate';
import GroupDetails from './components/GroupDetails';
import TransactionForm from './components/TransactionForm';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login setToken={setToken} />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/dashboard" element={<Dashboard token={token} />} />
        <Route path="/groups/create" element={<GroupCreate token={token} />} />
        <Route path="/groups/:id" element={<GroupDetails token={token} />} />
        <Route path="/transactions" element={<TransactionForm token={token} />} />
      </Routes>
    </Router>
  );
}

export default App;