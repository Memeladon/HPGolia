import { Button, ButtonGroup, Heading, VStack } from '@chakra-ui/react';
import React, { useState } from 'react';

export default function Home() {
  const [random, setRandom] = useState(0);
  const [count, setCount] = useState(0);

  return (
    <VStack>
      <Heading
        as='h1'
        size='4xl'
        bgGradient='linear(to-l, #7928CA, #FF0080)'
        bgClip='text'
      >
        Welcome to HPGolia!
      </Heading>

      <ButtonGroup>
        <Button
          onClick={() => {
            setRandom(Math.random() * 1000 + 2);
          }}
        >
          Ok {random}
        </Button>

        <Button
          fontWeight='extrabold'
          onClick={() => {
            setCount((prev) => prev + 1);
          }}
        >
          Count: {count}
        </Button>
      </ButtonGroup>
    </VStack>
  );
}
