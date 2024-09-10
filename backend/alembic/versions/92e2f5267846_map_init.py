"""map init

Revision ID: 92e2f5267846
Revises: 5a6eccacaa96
Create Date: 2024-09-09 10:24:01.941536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table

# revision identifiers, used by Alembic.
revision: str = '92e2f5267846'
down_revision: Union[str, None] = '5a6eccacaa96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

CELL = table("cell", sa.Column('id', sa.Integer(), nullable=False),
             sa.Column('position', sa.Integer(), nullable=False),
             sa.Column('title', sa.String(), nullable=False),
             sa.Column('type', sa.String(), nullable=False),
             sa.Column('background_img', sa.String(), nullable=True),
             sa.Column('main_conditions', sa.String(), nullable=False),
             sa.Column('genre_conditions', sa.String(), nullable=False)
             )

CELLS_DATA = [
    {
        'position': 0,
        'title': 'START',
        'type': 'START',
        'background_img': 'public/img/cells/start.png',
        'main_conditions': '{"event": "+ 5 Победных очков"}',
        'genre_conditions': '{}'
    },
    {
        'position': 1,
        'title': 'Kalawar (Alawar)',
        'type': 'GAME',
        'background_img': 'public/img/cells/kalawar.png',
        'main_conditions': '{"duration": "1-4", "price": "0-6"}',
        'genre_conditions': '{"tags": ["Point & Click", "Point-and-click"]}'
    },
    {
        'position': 2,
        'title': 'Подлянка/Кайфарик 1',
        'type': 'LUCKY_UNLUCKY',
        'background_img': None,
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 3,
        'title': 'THREE-DP (FIVE-BN)',
        'type': 'GAME',
        'background_img': 'public/img/cells/three-dp.png',
        'main_conditions': '{"duration": "2-5", "price": "5-12"}',
        'genre_conditions': '{"tags": ["Point & Click", "Point-and-click"]}'
    },
    {
        'position': 4,
        'title': 'YEA GAMES (EA GAMES)',
        'type': 'GAME',
        'background_img': 'public/img/cells/yea-games.png',
        'main_conditions': '{"duration": "1-5", "price": "7-15"}',
        'genre_conditions': '{"tags": ["FPS", "Shooter"]}'
    },
    {
        'position': 5,
        'title': 'Вопросик 1',
        'type': 'RANDOM',
        'background_img': 'public/img/cells/question-cell-ka.png',
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 6,
        'title': 'DYDOCE (DICE)',
        'type': 'GAME',
        'background_img': 'public/img/cells/dydoce.png',
        'main_conditions': '{"duration": "2-7", "price": "0-8"}',
        'genre_conditions': '{"tags": ["FPS", "Shooter"]}'
    },
    {
        'position': 7,
        'title': 'BIG DISH (BIG FISH)',
        'type': 'GAME',
        'background_img': 'public/img/cells/big-cock-dish-lmao-----hyyyyyyyyyype.png',
        'main_conditions': '{"duration": "3-7", "price": "0-10"}',
        'genre_conditions': '{"tags": ["Point & Click", "Point-and-click"]}'
    },
    {
        'position': 8,
        'title': 'Deactivision (Activision)',
        'type': 'GAME',
        'background_img': 'public/img/cells/deactivisionXXX.png',
        'main_conditions': '{"duration": "3-8", "price": "10-20"}',
        'genre_conditions': '{"tags": ["FPS", "Shooter"]}'
    },
    {
        'position': 9,
        'title': 'Pornstar Games (Rockstar Games)',
        'type': 'GAME',
        'background_img': 'public/img/cells/rock.png',
        'main_conditions': '{"duration": "4-10", "price": "15-30"}',
        'genre_conditions': '{"tags": ["FPS", "Shooter"]}'
    },
    {
        'position': 10,
        'title': 'ТЮРЯГА',
        'type': 'JAIL',
        'background_img': 'public/img/cells/.png',
        'main_conditions': '{"duration": "6-16"}',
        'genre_conditions': '{}'
    },
    {
        'position': 11,
        'title': 'Naughty boy (Naughty dog)',
        'type': 'GAME',
        'background_img': 'public/img/cells/naughtyboy.png',
        'main_conditions': '{"duration": "3-7", "rating": "40-80"}',
        'genre_conditions': '{"tags": ["Platformer", "3D Platformer"]}'
    },
    {
        'position': 12,
        'title': 'Подлянка/Кайфарик 2',
        'type': 'LUCKY_UNLUCKY',
        'background_img': None,
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 13,
        'title': 'PoroSad Studio (SadSquare Studio)',
        'type': 'GAME',
        'background_img': 'public/img/cells/.png',
        'main_conditions': '{"duration": "4-8", "price": "7-15"}',
        'genre_conditions': '{"tags": ["Psychological Horror", "Survival Horror", "Horror"]}'
    },
    {
        'position': 14,
        'title': 'SIGA (SEGA)',
        'type': 'GAME',
        'background_img': 'public/img/cells/porosad.png',
        'main_conditions': '{"duration": "4-8", "price": "0-7"}',
        'genre_conditions': '{"price": "10-20", "tags": ["Platformer", "3D Platformer"]}'
    },
    {
        'position': 15,
        'title': 'Вопросик 2',
        'type': 'RANDOM',
        'background_img': 'public/img/cells/question-cell-ka.png',
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 16,
        'title': 'CUMCOM (CAPCOM)',
        'type': 'GAME',
        'background_img': 'public/img/cells/cumcom.png',
        'main_conditions': '{"duration": "5-10", "price": "0-15"}',
        'genre_conditions': '{"duration": "4-10", "tags": ["Psychological Horror", "Survival Horror", "Horror"]}'
    },
    {
        'position': 17,
        'title': 'Team Plum (Team Cherry)',
        'type': 'GAME',
        'background_img': 'public/img/cells/team-plum.png',
        'main_conditions': '{"duration": "5-10"}',
        'genre_conditions': '{"duration": "5-10", "tags": ["Platformer", "3D Platformer"]}'
    },
    {
        'position': 18,
        'title': 'Team Vegan (Team Meat)',
        'type': 'GAME',
        'background_img': 'public/img/cells/green-meat-boy-with-fork.png',
        'main_conditions': '{"duration": "7-15", "price": "15-30"}',
        'genre_conditions': '{"duration": "8-300", "tags": ["Platformer", "3D Platformer"]}'
    },
    {
        'position': 19,
        'title': 'Red Head (Red Barrels)',
        'type': 'GAME',
        'background_img': 'public/img/cells/read-heads.png',
        'main_conditions': '{"duration": "7-15", "price": "0-15"}',
        'genre_conditions': '{"duration": "7-300", "tags": ["Psychological Horror", "Survival Horror", "Horror"]}'
    },
    {
        'position': 20,
        'title': 'Аукошная',
        'type': 'AUCTION',
        'background_img': 'public/img/cells/auk.png',
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 21,
        'title': 'LEGKO (LEGO)',
        'type': 'GAME',
        'background_img': 'public/img/cells/legko.png',
        'main_conditions': '{"rating": "45-85", "price": "15-35"}',
        'genre_conditions': '{"tags": ["Puzzle"]}'
    },
    {
        'position': 22,
        'title': 'Подлянка/Кайфарик 3',
        'type': 'LUCKY_UNLUCKY',
        'background_img': None,
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 23,
        'title': 'Microguy Games (SuperGiant Games)',
        'type': 'GAME',
        'background_img': 'public/img/cells/microguygames.png',
        'main_conditions': '{"duration": "7-14"}',
        'genre_conditions': '{"tags": ["Rogue-like", "Roguelike"]}'
    },
    {
        'position': 24,
        'title': 'Noproofs Games (Fireproof Games)',
        'type': 'GAME',
        'background_img': 'public/img/cells/noproof-games.png',
        'main_conditions': '{"duration": "6-12", "rating": "30-70"}',
        'genre_conditions': '{"duration": "7-14", "tags": ["Puzzle"]}'
    },
    {
        'position': 25,
        'title': 'Вопросик 3',
        'type': 'RANDOM',
        'background_img': 'public/img/cells/question-cell-ka.png',
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 26,
        'title': 'Bondage Nyamca (Bandai Namco)',
        'type': 'GAME',
        'background_img': 'public/img/cells/bondage.png',
        'main_conditions': '{"price": "7-20"}',
        'genre_conditions': '{"duration": "8-18", "tags": ["Anime"]}'
    },
    {
        'position': 27,
        'title': 'Leather club door (Cellar Door Games)',
        'type': 'GAME',
        'background_img': 'public/img/cells/clubdoor.png',
        'main_conditions': '{"duration": "8-16", "price": "10-30"}',
        'genre_conditions': '{"duration": "8-300", "tags": ["Rogue-like", "Roguelike"]}'
    },
    {
        'position': 28,
        'title': 'Vlomve (Valve)',
        'type': 'GAME',
        'background_img': 'public/img/cells/vlomve.png',
        'main_conditions': '{"duration": "9-17", "price": "20-40"}',
        'genre_conditions': '{"duration": "9-300", "tags": ["Puzzle"]}'
    },
    {
        'position': 29,
        'title': 'Kawaimi (Konami)',
        'type': 'GAME',
        'background_img': 'public/img/cells/kawaimi.png',
        'main_conditions': '{"duration": "12-20", "price": "10-20"}',
        'genre_conditions': '{"tags": ["Platformer", "3D Platformer"]}'
    },
    {
        'position': 30,
        'title': 'Лотерея',
        'type': 'LOTTERY',
        'background_img': 'public/img/cells/topori.png',
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 31,
        'title': 'Besedka (Bethesda)',
        'type': 'GAME',
        'background_img': 'public/img/cells/besedka.png',
        'main_conditions': '{"duration": "8-14", "rating": "25-65"}',
        'genre_conditions': '{"duration": "10-20", "tags": ["RPG", "Action RPG", "JRPG", "Tactical RPG"]}'
    },
    {
        'position': 32,
        'title': 'Подлянка/Кайфарик 4',
        'type': 'LUCKY_UNLUCKY',
        'background_img': None,
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 33,
        'title': 'Squidwardix (SquareEnix)',
        'type': 'GAME',
        'background_img': 'public/img/cells/squidwardix.png',
        'main_conditions': '{"rating": "20-70", "price": "20-100"}',
        'genre_conditions': '{"rating": "20-60", "tags": ["RPG", "Action RPG", "JRPG", "Tactical RPG"]}'
    },
    {
        'position': 34,
        'title': 'DVD PROJECT BRED (CD PROJECT RED)',
        'type': 'GAME',
        'background_img': 'public/img/cells/bred.png',
        'main_conditions': '{"duration": "10-18", "price": "10-25"}',
        'genre_conditions': '{"price": "25-100", "tags": ["RPG", "Action RPG", "JRPG", "Tactical RPG"]}'
    },
    {
        'position': 35,
        'title': 'Вопросик 4',
        'type': 'RANDOM',
        'background_img': 'public/img/cells/question-cell-ka.png',
        'main_conditions': '{}',
        'genre_conditions': '{}'
    },
    {
        'position': 36,
        'title': 'Chelic Entertainment (Relic Entertainment)',
        'type': 'GAME',
        'background_img': 'public/img/cells/chelic.png',
        'main_conditions': '{"duration": "10-20", "price": "0-25"}',
        'genre_conditions': '{"duration": "10-20", "tags": ["Turn-Based Strategy", "Strategy", "Strategy RPG"]}'
    },
    {
        'position': 37,
        'title': 'Kunisoft (Ubisoft)',
        'type': 'GAME',
        'background_img': 'public/img/cells/kunisoft.png',
        'main_conditions': '{"duration": "10-20", "price": "25-100"}',
        'genre_conditions': '{"duration": "14-1000", "tags": ["RPG", "Action RPG", "JRPG", "Tactical RPG"]}'
    },
    {
        'position': 38,
        'title': 'Piratix Games (Firaxis Games)',
        'type': 'GAME',
        'background_img': 'public/img/cells/piratix.png',
        'main_conditions': '{"price": "30-100"}',
        'genre_conditions': '{"rating": "55-85", "tags": ["Turn-Based Strategy", "Strategy", "Strategy RPG"]}'
    },
    {
        'position': 39,
        'title': 'Blazerd (Blizzard)',
        'type': 'GAME',
        'background_img': 'public/img/cells/blazerd.png',
        'main_conditions': '{"duration": "14-300"}',
        'genre_conditions': '{"duration": "16-300", "tags": ["Turn-Based Strategy", "Strategy", "Strategy RPG"]}'
    }]


def upgrade() -> None:
    # op.bulk_insert(CELL, CELLS_DATA)
    op.bulk_insert(CELL, CELLS_DATA)
    pass


def downgrade() -> None:
    op.execute(CELL.delete())
    pass
