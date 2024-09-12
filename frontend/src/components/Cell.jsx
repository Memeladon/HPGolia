import { Center, Image } from '@chakra-ui/react';
import { constants } from '../debug';

export default function Cell({ cellData, imgSrc }) {
  return (
    <Center bgColor={'teal'} className='cell-container'>
      <Image
        maxWidth={'60%'}
        src={imgSrc || constants.map.defaultImgSrc}
        alt='Dan Abramov'
      />
    </Center>
  );
}
