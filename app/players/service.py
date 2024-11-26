from app.players.model import Player
from constant import *
from database import get_connection


# класс для работы с одноименной таблицей БД
class PlayerService:

    # функция для работы с изменением данных в таблице
    @staticmethod
    def register_player(player: Player):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO players (nick_name, hero_id, feedback) VALUES (?, ?, ?)
            ''', (player.nick_name, player.hero_id, player.feedback))
            conn.commit()

    # функция для работы с получением всех данных в таблице
    @staticmethod
    def get_all_players():
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM players''').fetchall()
            return [Player(el[1], el[2], el[3], el[0]) for el in result]

    # функция для работы с получением по индификатору данных в таблице
    @staticmethod
    def get_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM players WHERE id = ?''', player_id).fetchone()
            if result:
                return Player(result[1], result[2], result[3], result[0])
            return

    # функция для работы с получением по имени данных в таблице
    @staticmethod
    def get_player_by_name(player_name: str):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM players WHERE nick_name = ?''', (player_name,)).fetchone()
            if result:
                return Player(result[1], result[2], result[3], result[0])
            return None

    # функция для работы с удалением по индификатору данных в таблице
    @staticmethod
    def drop_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''DELETE FROM players WHERE id = ?'''
            , player_id)
            conn.commit()
