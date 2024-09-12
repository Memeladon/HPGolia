import {
  Button,
  Flex,
  FormControl,
  FormLabel,
  Heading,
  Input,
  Stack,
  useColorModeValue,
} from '@chakra-ui/react';
import React, { useContext, useEffect, useState } from 'react';
import { Form, useNavigate } from 'react-router-dom';
import { UserContext } from '../providers/context/UserContext';
import Cookies from 'js-cookie';
import axios from 'axios';
import { constants } from '../debug';

export default function Login() {
  const navigate = useNavigate();

  const { user, setUser, accessToken, setAccessToken } =
    useContext(UserContext);

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const [invalidPassword, setInvalidPassword] = useState(false);
  const [invalidUsername, setInvalidUsername] = useState(false);

  useEffect(() => {
    if (accessToken) {
      navigate('/');
    }
  }, [user, accessToken]);

  useEffect(() => {
    setInvalidUsername(!username?.length);
  }, [username]);

  useEffect(() => {
    setInvalidPassword(!password?.length);
  }, [password]);

  const onSubmit = () => {
    (async () => {
      if (invalidPassword || invalidUsername) return;

      try {
        const response = await axios.postForm(
          `${constants.baseUrl}/auth/token`,
          {
            grant_type: 'password',
            username: username,
            password: password,
          }
        );

        const { data } = response;

        if (!data.access_token || !data.access_token?.length) {
          throw new Error('no access token provided');
        }

        Cookies.set('access_token', data.access_token, { expires: 14 });
        Cookies.set('token_type', data.token_type, { expires: 14 });

        setAccessToken(data.access_token);
      } catch (e) {
        console.error('error fetch auth', e);
        alert(JSON.stringify(e?.response?.data));

        setUsername('');
        setPassword('');
      }
    })();
  };

  return (
    <Flex
      minH={'50vh'}
      align={'center'}
      justify={'center'}
      bg={useColorModeValue('gray.50', 'gray.800')}
    >
      <Stack
        spacing={4}
        w={'full'}
        maxW={'md'}
        bg={useColorModeValue('white', 'gray.700')}
        rounded={'xl'}
        boxShadow={'lg'}
        p={6}
        my={12}
      >
        <Heading lineHeight={1.1} fontSize={{ base: '2xl', md: '3xl' }}>
          Login
        </Heading>
        <FormControl
          id='email'
          isRequired={invalidUsername}
          isInvalid={invalidUsername}
        >
          <FormLabel>Username</FormLabel>
          <Input
            placeholder='username'
            _placeholder={{ color: 'gray.500' }}
            type='text'
            // @ts-ignore
            onChange={(e) => setUsername(e.target.value)}
            value={username}
          />
        </FormControl>
        <FormControl
          id='password'
          isRequired={invalidPassword}
          isInvalid={invalidPassword}
        >
          <FormLabel>Password</FormLabel>
          <Input
            type='password'
            // @ts-ignore
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          />
        </FormControl>
        <Stack spacing={6}></Stack>
        <Button
          onClick={onSubmit}
          bg={'purple.700'}
          color={'white'}
          _hover={{
            bg: 'purple.600',
          }}
        >
          Submit
        </Button>
      </Stack>
    </Flex>
  );
}
