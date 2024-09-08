import { Box, Flex, HStack, useColorModeValue } from '@chakra-ui/react';
import React from 'react';
import { Link, Outlet } from 'react-router-dom';

function NavItem({ to, children }) {
  return (
    <Link to={to}>
      <Box fontWeight='bold' p='2' rounded='md' _hover={{ bg: 'gray.600' }}>
        {children}
      </Box>
    </Link>
  );
}

export default function Navbar() {
  return (
    <>
      <>
        <Box bg={useColorModeValue('gray.100', 'gray.900')} px={4} mb={4}>
          <Flex h={12} alignItems={'center'} justifyContent={'space-between'}>
            <HStack spacing={8} alignItems={'center'}>
              <HStack
                as={'nav'}
                spacing={4}
                display={{ base: 'none', md: 'flex' }}
              >
                <NavItem to='/'>Home</NavItem>
                <NavItem to='/game'>Game</NavItem>
              </HStack>
            </HStack>
          </Flex>
        </Box>
      </>
      <Outlet />
    </>
  );
}
