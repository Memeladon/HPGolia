import Navbar from './components/Navbar';
import './App.css';

import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import NotFound from './pages/NotFound';
import React, { useEffect, useState } from 'react';
import Login from './pages/Login';
import User from './pages/User';
import Session from './pages/Session';
import { MapContext } from './providers/context/MapContext';
import { constants } from './debug';
import axios from 'axios';
import { UserContext } from './providers/context/UserContext';
import Cookies from 'js-cookie';

function App() {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState(null);

  const [cells, setCells] = useState([]);

  useEffect(() => {
    const cookieFound = Cookies.get('access_token');
    if (cookieFound && cookieFound.length) {
      setAccessToken(cookieFound);
    }

    //TODO: get the user here (by cookie) when the endpoints are secured
  }, []);

  useEffect(() => {
    (async () => {
      if (!accessToken) return;

      try {
        const response = await axios.get(
          `${constants.baseUrl}/session-map/cells`
        );

        setCells(
          response.data.map((cell) => {
            let backgroundImg = cell.background_img;

            if (backgroundImg && backgroundImg.includes('/')) {
              const imgTitle = backgroundImg.split('/').pop();

              // добавил это т.к. может приходить "cells/.png"
              backgroundImg = imgTitle.startsWith('.')
                ? null
                : `${constants.baseUrl}/storage/cells/${imgTitle}`;
            }

            cell.background_img = backgroundImg;
            return cell;
          })
        );
      } catch (e) {
        console.error('error fetch cells', e);
      }
    })();
  }, [accessToken]);

  return (
    <>
      <UserContext.Provider
        value={{ user, setUser, accessToken, setAccessToken }}
      >
        <MapContext.Provider value={{ cells, setCells }}>
          <Routes>
            {accessToken ? (
              <Route element={<Navbar />}>
                <Route index element={<Home />} />
                <Route path='/login' element={<Login />} />
                <Route path='/user' element={<User />} />
                <Route path='/session' element={<Session />} />
                <Route path='*' element={<NotFound />} />
              </Route>
            ) : (
              <Route element={<Navbar />}>
                <Route path='*' element={<Login />} />
              </Route>
            )}
          </Routes>
        </MapContext.Provider>
      </UserContext.Provider>
    </>
  );
}

export default App;
