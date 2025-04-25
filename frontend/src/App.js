import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    product: '',
  });
  const [response, setResponse] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('https://r0751wvqef.execute-api.us-east-1.amazonaws.com', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });
    const result = await res.json();
    setResponse(result.message);
  };

  return (
    <div className="App">
      <h1>QuickKart Order Form</h1>
      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" onChange={handleChange} required />
        <input name="email" placeholder="Email" onChange={handleChange} required />
        <input name="product" placeholder="Product" onChange={handleChange} required />
        <button type="submit">Submit Order</button>
      </form>
      <p>{response}</p>
    </div>
  );
}

export default App;
