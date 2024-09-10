import Navbar from './components/common/Navbar';
import './App.css';

import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import NotFound from './pages/NotFound';
import React from 'react';
import Login from './pages/Login';
import User from './pages/User';
import Session from './pages/Session';

function App() {
  return (
    <>
      <Routes>
        <Route element={<Navbar />}>
          <Route index element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/user' element={<User />} />
          <Route path='/session' element={<Session />} />
          <Route path='*' element={<NotFound />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
