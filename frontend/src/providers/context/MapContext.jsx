import { createContext, useContext } from 'react';

export const MapContext = createContext({
  cells: null,
  setCells: (c) => c,
});
