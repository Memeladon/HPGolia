from ..crud import create_fields
from ..models import FieldType
import json


def init_fields(db):
    fields_data = [
        {"name": "START", "field_type": FieldType.START, "data": json.dumps({"event": "+ 5 Победных очков"})},  # 0
        {"name": "Kalawar (Alawar)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "1-4", "price": "0-6"},
            "additional": {"duration": "2-6", "tegs": "Point & Click, Point-and-click"}
        })},  # 1
        {"name": "Подлянка/Кайфарик 1", "field_type": FieldType.LUCKY_UNLUCKY,
         "data": json.dumps({"event": "Крути колесико подлянок/кайфариков!"})},  # 2
        {"name": "THREE-DP (FIVE-BN)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "2-5", "price": "5-12"},
            "additional": {"duration": "4-8", "tegs": "Point & Click, Point-and-click"}
        })},  # 3
        {"name": "YEA GAMES (EA GAMES)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "1-5", "price": "7-15"},
            "additional": {"duration": "2-7", "tegs": "FPS, Shooter"}
        })},  # 4
        {"name": "Вопросик 1", "field_type": FieldType.RANDOM,
         "data": json.dumps({"event": "Просто крути колесо игр без параметров!"})},  # 5
        {"name": "DYDOCE (DICE)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "2-7", "price": "0-8"},
            "additional": {"duration": "4-9", "tegs": "FPS, Shooter"}
        })},  # 6
        {"name": "BIG DISH (BIG FISH)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "3-7", "price": "0-10"},
            "additional": {"duration": "5-300", "tegs": "Point & Click, Point-and-click"}
        })},  # 7
        {"name": "Deactivision (Activision)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "3-8", "price": "10-20"},
            "additional": {"duration": "5-12", "tegs": "FPS, Shooter"}
        })},  # 8
        {"name": "Pornstar Games (Rockstar Games)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "4-10", "price": "15-30"},
            "additional": {"duration": "6-300", "tegs": "FPS, Shooter"}
        })},  # 9
        {"name": "ТЮРЯГА", "field_type": FieldType.JAIL, "data": json.dumps({"main": {"duration": "6-16"}})},  # 10
        {"name": "Naughty boy (Naughty dog)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "3-7", "rating": "40-80"},
            "additional": {"duration": "5-300", "tegs": "Platformer, 3D Platformer"}
        })},  # 11
        {"name": "Подлянка/Кайфарик 2", "field_type": FieldType.LUCKY_UNLUCKY, "data": None},  # 12
        {"name": "PoroSad Studio (SadSquare Studio)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "4-8", "price": "7-15"},
            "additional": {"tegs": "Psychological Horror, Survival Horror, Horror"}
        })},  # 13
        {"name": "SIGA (SEGA)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "4-8", "price": "0-7"},
            "additional": {"price": "10-20", "tegs": "Platformer, 3D Platformer"}
        })},  # 14
        {"name": "Вопросик 2", "field_type": FieldType.RANDOM,
         "data": json.dumps({"event": "Просто крути колесо игр без параметров!"})},  # 15
        {"name": "CUMCOM (CAPCOM)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "5-10", "price": "0-15"},
            "additional": {"duration": "4-10", "tegs": "Psychological Horror, Survival Horror, Horror"}
        })},  # 16
        {"name": "Team Plum (Team Cherry)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "5-10"},
            "additional": {"duration": "5-10", "tegs": "Platformer, 3D Platformer"}
        })},  # 17
        {"name": "Team Vegan (Team Meat)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "7-15", "price": "15-30"},
            "additional": {"duration": "8-300", "tegs": "Platformer, 3D Platformer"}
        })},  # 18
        {"name": "Red Head (Red Barrels)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "7-15", "price": "0-15"},
            "additional": {"duration": "7-300", "tegs": "Psychological Horror, Survival Horror, Horror"}
        })},  # 19
        {"name": "Аукошная", "field_type": FieldType.AUCTION,
         "data": json.dumps({"event": "Договаривайся с Начальником аука"})},  # 20
        {"name": "LEGKO (LEGO)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"rating": "45-85", "price": "15-35"},
            "additional": {"tegs": "Puzzle"}
        })},  # 21
        {"name": "Подлянка/Кайфарик 3", "field_type": FieldType.LUCKY_UNLUCKY,
         "data": json.dumps({"event": "Крути колесико подлянок/кайфариков!"})},  # 22
        {"name": "Microguy Games (SuperGiant Games)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "7-14"},
            "additional": {"tegs": "Rogue-like, Roguelike"}
        })},  # 23
        {"name": "Noproofs Games (Fireproof Games)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "6-12", "rating": "30-70"},
            "additional": {"duration": "7-14", "tegs": "Puzzle"}
        })},  # 24
        {"name": "Вопросик 3", "field_type": FieldType.RANDOM,
         "data": json.dumps({"event": "Просто крути колесо игр без параметров!"})},  # 25
        {"name": "Bondage Nyamca (Bandai Namco)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"price": "7-20"},
            "additional": {"duration": "8-18", "tegs": "Anime"}
        })},  # 26
        {"name": "Leather club door (Cellar Door Games)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "8-16", "price": "10-30"},
            "additional": {"duration": "8-1000", "tegs": "Rogue-like, Roguelike"}
        })},  # 27
        {"name": "Vlomve (Valve)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "9-17", "price": "20-40"},
            "additional": {"duration": "9-1000", "tegs": "Puzzle"}
        })},  # 28
        {"name": "Kawaimi (Konami)", "field_type": FieldType.GAME, "data": json.dumps({
            "main": {"duration": "12-20", "price": "10-20"},
            "additional": {"tegs": "Platformer, 3D Platformer"}
        })},  # 29
        {"name": "Лотерея", "field_type": FieldType.LOTTERY, "data": json.dumps({"event": "777"})},  # 30 LOTTERY
        {"name": "Besedka (Bethesda)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"duration": "8-14", "rating": "25-65"},
                             "additional": {"duration": "10-20", "tegs": "RPG, Action RPG, JRPG, Tactical RPG"}})},
        # 31 GAME
        {"name": "Подлянка/Кайфарик 4", "field_type": FieldType.LUCKY_UNLUCKY,
         "data": json.dumps({"event": "Крути колесико подлянок/кайфариков!"})},  # 32 LUCKY OR UNLUCKY
        {"name": "Squidwardix (SquareEnix)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"rating": "20-70", "price": "20-100"},
                             "additional": {"rating": "20-60", "tegs": "RPG, Action RPG, JRPG, Tactical RPG"}})},
        # 33 GAME
        {"name": "DVD PROJECT BRED (CD PROJECT RED)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"duration": "10-18", "price": "10-25"},
                             "additional": {"price": "25-100", "tegs": "RPG, Action RPG, JRPG, Tactical RPG"}})},
        # 34 GAME
        {"name": "Вопросик 4", "field_type": FieldType.RANDOM,
         "data": json.dumps({"event": "Просто крути колесо игр без параметров!"})},  # 35 RANDOM
        {"name": "Chelic Entertainment (Relic Entertainment)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"duration": "10-20", "price": "0-25"},
                             "additional": {"duration": "10-20",
                                            "tegs": "Turn-Based Strategy, Strategy, Strategy RPG"}})},  # 36 GAME
        {"name": "Kunisoft (Ubisoft)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"duration": "10-20", "price": "25-100"},
                             "additional": {"duration": "14-1000", "tegs": "RPG, Action RPG, JRPG, Tactical RPG"}})},
        # 37 GAME
        {"name": "Piratix Games (Firaxis Games)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"price": "30-100"},
                             "additional": {"rating": "55-85",
                                            "tegs": "Turn-Based Strategy, Strategy, Strategy RPG"}})},  # 38 GAME
        {"name": "Blazerd (Blizzard)", "field_type": FieldType.GAME,
         "data": json.dumps({"main": {"duration": "14-300"},
                             "additional": {"duration": "16-300",
                                            "tegs": "Turn-Based Strategy, Strategy, Strategy RPG"}})},  # 39 GAME
        ]
    create_fields(fields_data, db)
