import Home from './pages/Home';
import Navbar from './components/common/Navbar';
import './App.css';

import React from 'react';

import { Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <>
      <Routes>
        <Route element={<Navbar />}>
          <Route path='/' element={<Home />}></Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
