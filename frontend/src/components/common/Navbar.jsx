import { Text } from '@chakra-ui/react';
import React from 'react';
import { Outlet } from 'react-router-dom';

export default function Navbar() {
  return (
    <>
      <Text as='span'>Navbar will be here</Text>
      <Outlet />
    </>
  );
}
