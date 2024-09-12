import { createContext, useContext } from 'react';

export const UserContext = createContext({
  user: null,
  setUser: (u) => u,
  accessToken: null,
  setAccessToken: (a) => a,
});
