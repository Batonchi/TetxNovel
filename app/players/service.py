from app.players.model import Player
from constant import *
from database import get_connection
# класс работающий с БД с таблицей items


class PlayerService:

    @staticmethod
    def register_player(player: Player):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO players (nick_name, hero_id, feedback) VALUES (?, ?, ?)
            ''', (player.nick_name, player.hero_id, player.feedback))
            conn.commit()

    @staticmethod
    def get_all_players():
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM players''').fetchall()
            return [Player(el[1], el[2], el[3], el[0]) for el in result]

    @staticmethod
    def get_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM players WHERE id = ?''', player_id).fetchone()
            return Player(result[1], result[2], result[3], result[0])

    @staticmethod
    def get_player_by_name(player_name: str):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute(f'''SELECT * FROM players WHERE nick_name = ?''', player_name).fetchone()
            return Player(result[1], result[2], result[3], result[0])

    @staticmethod
    def drop_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''DELETE FROM players WHERE id = ?'''
            , player_id)
            conn.commit()

    @staticmethod
    def get_last_player_id():
        print(PATH)
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                SELECT id FROM players ORDER BY id DESC LIMIT 1
            ''').fetchone()
