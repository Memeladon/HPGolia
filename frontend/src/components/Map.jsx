import React from 'react';

import Cell from './Cell';

import { constants } from '../debug';
import {
  Box,
  Center,
  Flex,
  Grid,
  GridItem,
  Heading,
  VStack,
} from '@chakra-ui/react';

export default function Map() {
  const mapCells = [[], [], [], []];

  const parts = 4;
  const sliceNum = constants.map.cells.length / 4;

  for (let part = 0; part < parts; part++) {
    const sliceStart = part * sliceNum;
    mapCells[part] = constants.map.cells.slice(
      sliceStart,
      sliceStart + sliceNum
    );
  }

  return (
    <Box className='session-map-container'>
      <Center className='session-map'>
        <Box className='cells-container' maxWidth={'80%'}>
          <Grid
            gridTemplateColumns={`repeat(${sliceNum}, 1fr)`}
            gridTemplateRows={`repeat(${sliceNum}, 1fr)`}
          >
            {}

            <GridItem
              className='upper-row'
              bgColor={'grey'}
              gridColumn={'1 / 11'}
              gridRow={'1 / 1'}
            >
              <Center>
                <Flex flexFlow={'row'} gap={2}>
                  {mapCells[0].map((cell, i) => {
                    return <Cell cellData={cell} key={cell.id}></Cell>;
                  })}
                </Flex>
              </Center>
            </GridItem>
            <GridItem
              className='void'
              bgColor={'black'}
              gridColumn={'2 / 10'}
              gridRow={'2 / 10'}
            />
            <GridItem
              className='right-column'
              gridColumn={'10 / 10'}
              gridRow={'2 / 10'}
              bgColor={'grey'}
            >
              <Center>
                <Flex flexFlow={'column'} gap={2}>
                  {mapCells[1].map((cell, i) => {
                    return <Cell cellData={cell} key={cell.id}></Cell>;
                  })}
                </Flex>
              </Center>
            </GridItem>
            <GridItem
              bgColor={'grey'}
              gridColumn={'1 / 11'}
              gridRow={'10 / 10'}
            >
              <Center>
                <Flex flexFlow={'row-reverse'} gap={2}>
                  {mapCells[2].map((cell, i) => {
                    return <Cell cellData={cell} key={cell.id}></Cell>;
                  })}
                </Flex>
              </Center>
            </GridItem>
            <GridItem bgColor={'grey'} gridColumn={'1 / 1'} gridRow={'2 / 10'}>
              <Center>
                <Flex flexFlow={'column-reverse'} gap={2}>
                  {mapCells[3].map((cell, i) => {
                    return <Cell cellData={cell} key={cell.id}></Cell>;
                  })}
                </Flex>
              </Center>
            </GridItem>
          </Grid>
        </Box>
      </Center>
    </Box>
  );
}
