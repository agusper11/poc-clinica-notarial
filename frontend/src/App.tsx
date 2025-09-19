import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/status')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => setMessage('Error al conectar con backend'));
  }, []);

  return (
    <div className="App">
      <h1>Sistema Clínica Notarial - PoC</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;

