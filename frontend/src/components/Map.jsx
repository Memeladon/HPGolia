import { useContext, useEffect, useMemo, useState } from 'react';

import Cell from './Cell';

import { Box, Center, Flex, Grid, GridItem, Spinner } from '@chakra-ui/react';
import { MapContext } from '../providers/context/MapContext';

export default function Map() {
  const parts = 4;

  const { cells } = useContext(MapContext);

  const [loading, setLoading] = useState(true);

  const sliceNum = useMemo(() => cells.length / 4, [cells]);

  const mapCells = useMemo(() => {
    let tempMap = [[], [], [], []];
    for (let part = 0; part < parts && sliceNum > 0; part++) {
      const sliceStart = part * sliceNum;
      tempMap[part] = cells.slice(sliceStart, sliceStart + sliceNum);
    }

    return tempMap;
  }, [cells]);

  useEffect(() => {
    setLoading(!cells.length);
  }, [cells]);

  return (
    <Box className='session-map-container'>
      {loading ? (
        <Spinner size={'xl'} ml={'auto'} />
      ) : (
        <Grid
          className='map'
          gridTemplateColumns={`repeat(${sliceNum}, 1fr)`}
          gridTemplateRows={`repeat(${sliceNum}, 1fr)`}
          gap={1}
        >
          <GridItem
            className='upper-row'
            gridColumn={'1 / 11'}
            gridRow={'1 / 1'}
          >
            <Center>
              <Flex flexFlow={'row'} gap={1}>
                {mapCells[0].map((cell, i) => {
                  return <Cell cellData={cell} key={cell.id}></Cell>;
                })}
              </Flex>
            </Center>
          </GridItem>
          <GridItem className='void' gridColumn={'2 / 10'} gridRow={'2 / 10'} />
          <GridItem
            className='right-column'
            gridColumn={'10 / 10'}
            gridRow={'2 / 10'}
          >
            <Center>
              <Flex flexFlow={'column'} gap={1}>
                {mapCells[1].map((cell, i) => {
                  return <Cell cellData={cell} key={cell.id}></Cell>;
                })}
              </Flex>
            </Center>
          </GridItem>
          <GridItem gridColumn={'1 / 11'} gridRow={'10 / 10'}>
            <Center>
              <Flex flexFlow={'row-reverse'} gap={1}>
                {mapCells[2].map((cell, i) => {
                  return <Cell cellData={cell} key={cell.id}></Cell>;
                })}
              </Flex>
            </Center>
          </GridItem>
          <GridItem gridColumn={'1 / 1'} gridRow={'2 / 10'}>
            <Center>
              <Flex flexFlow={'column-reverse'} gap={1}>
                {mapCells[3].map((cell, i) => {
                  return <Cell cellData={cell} key={cell.id}></Cell>;
                })}
              </Flex>
            </Center>
          </GridItem>
        </Grid>
      )}
    </Box>
  );
}
