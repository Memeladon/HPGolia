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
import React from 'react';
import { Link, Outlet } from 'react-router-dom';

import logo from '../../public/img/logo.jpg';
import { constants } from '../../debug';
import { MoonIcon, SunIcon } from '@chakra-ui/icons';

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
  const { colorMode, toggleColorMode } = useColorMode();

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
                // colorScheme='teal'
                icon={colorMode === 'dark' ? <SunIcon /> : <MoonIcon />}
                aria-label={'Toogle color scheme'}
                onClick={toggleColorMode}
              ></IconButton>
            </HStack>
          </Box>
        </Flex>
      </Box>
      {/* OTHER PART OF THE WEB PAGE */}
      <Outlet />
    </>
  );
}
