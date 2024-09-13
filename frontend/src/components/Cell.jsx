import { Center, HStack, Image, VStack } from '@chakra-ui/react';
import { constants } from '../debug';

export default function Cell({ cellData }) {
  return (
    <VStack
      backgroundColor={'gray.500'}
      className='cell-container'
      width={'7vw'}
      height={'7vh'}
    >
      <Image
        className='cell-img select-disable'
        draggable='false'
        display={'block'}
        width={'auto'}
        height={'100%'}
        src={cellData.background_img}
        alt={`${cellData.title}`}
      />
    </VStack>
  );
}
