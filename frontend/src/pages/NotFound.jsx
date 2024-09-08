import { Heading, Icon, useColorModeValue, VStack } from '@chakra-ui/react';
import { ViewIcon } from '@chakra-ui/icons';
import React from 'react';

export default function Home() {
  return (
    <>
      <VStack>
        <Heading textColor='red.500' as='h1' size='4xl'>
          <Icon as={ViewIcon}></Icon>
        </Heading>
        <Heading as='h1' size='2xl'>
          Where are you going?
        </Heading>
      </VStack>
    </>
  );
}
