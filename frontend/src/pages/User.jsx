'use client';

import {
  Badge,
  Button,
  Center,
  Flex,
  Heading,
  Image,
  Stack,
  Text,
  useColorModeValue,
  VStack,
} from '@chakra-ui/react';
import React, { useEffect, useState } from 'react';
import { constants } from '../debug.js';
import axios from 'axios';

export default function User() {
  const [user, setUser] = useState({});

  useEffect(() => {
    (async () => {
      try {
        const response = await axios.get(
          `${constants.baseUrl}/users/${constants.user.id}`
        );

        response.data.logo = response.data.logo
          ? response.data.logo
          : constants.user.logo;

        setUser(response.data);
      } catch (e) {
        console.error(e);
      }
    })();
  }, []);

  return (
    <Center>
      <Stack
        borderWidth='1px'
        borderRadius='md'
        w={{ sm: '100%', md: '700px' }}
        height={{ sm: '476px', md: '20rem' }}
        direction={{ base: 'column', md: 'row' }}
        bg={useColorModeValue('white', 'gray.900')}
        boxShadow={'2xl'}
        padding={4}
      >
        <Flex mb={10}>
          <Stack>
            <Image
              objectFit='fill'
              boxSize='100%'
              src={
                // @ts-ignore
                user.logo
              }
              alt='logo'
            />
            <Button p={4}>New image</Button>
          </Stack>
        </Flex>
        <Stack
          flex={1}
          flexDirection='column'
          justifyContent='center'
          alignItems='center'
          p={1}
          pt={2}
        >
          <Heading fontSize={'2xl'} mb={'auto'}>
            {
              // @ts-ignore
              user.username
            }
          </Heading>
          {
            // @ts-ignore
            Object.entries(user).map(([key, value]) => {
              return (
                <Text key={key}>
                  {key} - {value}
                </Text>
              );
            })
          }
          <VStack></VStack>
        </Stack>
      </Stack>
    </Center>
  );
}
