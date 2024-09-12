import {
  Avatar,
  Box,
  Flex,
  HStack,
  Image,
  useColorModeValue,
  useColorMode,
  Wrap,
  WrapItem,
  IconButton,
} from '@chakra-ui/react';
import React, { useContext } from 'react';
import { Link, Outlet } from 'react-router-dom';

import logo from '../public/img/logo.jpg';
import { constants } from '../debug';
import { CloseIcon, MoonIcon, SunIcon } from '@chakra-ui/icons';
import { UserContext } from '../providers/context/UserContext';
import Cookies from 'js-cookie';

function NavItem({ to, children }) {
  return (
    <Link to={to}>
      <Box
        fontWeight='bold'
        padding={2}
        rounded='md'
        _hover={{ bg: 'gray.600' }}
      >
        {children}
      </Box>
    </Link>
  );
}

export default function Navbar() {
  const { accessToken, setAccessToken, setUser } = useContext(UserContext);

  const { colorMode, toggleColorMode } = useColorMode();

  const logOut = () => {
    Cookies.remove('token_type');
    Cookies.remove('access_token');

    setAccessToken(null);
    setUser(null);
  };

  return (
    <>
      <Box bg={useColorModeValue('gray.100', 'gray.900')} px={8} mb={8} py={2}>
        <Flex h={12} alignItems={'center'} justifyContent={'space-between'}>
          <HStack spacing={10} alignItems={'center'}>
            <HStack
              as={'nav'}
              spacing={4}
              display={{ base: 'none', md: 'flex' }}
            >
              <NavItem to='/'>
                <Image src={logo} alt='logo' boxSize='40px'></Image>
              </NavItem>
              <NavItem to='/session'>Session</NavItem>
            </HStack>
          </HStack>
          {accessToken && (
            <Box marginLeft={'auto'}>
              <HStack>
                <NavItem to='/user'>
                  <Wrap>
                    <WrapItem>
                      <Avatar src={constants.user.logo}></Avatar>
                    </WrapItem>
                  </Wrap>
                </NavItem>
                <IconButton
                  icon={colorMode === 'dark' ? <SunIcon /> : <MoonIcon />}
                  aria-label={'Toogle color scheme'}
                  onClick={toggleColorMode}
                ></IconButton>
                <IconButton
                  icon={<CloseIcon />}
                  aria-label={'Log out'}
                  onClick={logOut}
                ></IconButton>
              </HStack>
            </Box>
          )}
        </Flex>
      </Box>
      {/* OTHER PART OF THE WEB PAGE */}
      <Outlet />
    </>
  );
}
