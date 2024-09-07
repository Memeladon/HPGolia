import { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <h1>Welcome to HPGolia!</h1>
      <button
        onClick={() => {
          setCount(Math.random() * 1000 + 2);
        }}
      >
        Ok {count}
      </button>
    </>
  );
}

export default App;
