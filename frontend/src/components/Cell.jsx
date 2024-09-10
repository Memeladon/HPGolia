import { Box, Center, Heading, HStack, Image, VStack } from '@chakra-ui/react';
import React from 'react';

export default function Cell({ cellData }) {
  return (
    <Center bgColor={'teal'} className='cell-container'>
        <Image
          maxWidth={'60%'}
          src='https://www.w3schools.com/css/img_forest.jpg'
          alt='Dan Abramov'
        />
    </Center>
  );
}
