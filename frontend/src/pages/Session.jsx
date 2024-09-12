import { Box, Center, Heading } from '@chakra-ui/react';
import React from 'react';

import Map from '../components/Map';

export default function Session() {
  return (
    <Center className='session-container'>
      <Box maxWidth={'70%'} className='session'>
        <Map></Map>
      </Box>
    </Center>
  );
}
