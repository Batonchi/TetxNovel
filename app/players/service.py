from app.players.model import Player
from app.constant import *
from app.database import get_connection
# класс работающий с БД с таблицей items


class PlayerService:

    @staticmethod
    def register_player(player: Player):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO players (id, nick_name, hero_id, feedback) VALUES (?, ?, ?, ?)
            ''', (player.id, player.nick_name, player.hero_id, player.feedback))
            conn.commit()

    @staticmethod
    def get_all_players():
        with get_connection(PATH) as conn:
            return conn.cursor().execute(
                '''
                    SELECT * FROM players
                '''
            ).fetchall()

    @staticmethod
    def get_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            return conn.cursor().execute(
                '''
                SELECT * FROM players WHERE id = ?
                '''
            , player_id).fetchone()

    @staticmethod
    def get_player_by_name(player_name: str):
        with get_connection(PATH) as conn:
            return conn.cursor().execute(
                f'''SELECT * FROM players''').fetchone()

    @staticmethod
    def drop_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''DELETE FROM players WHERE id = ?'''
            , player_id)
            conn.commit()

    @staticmethod
    def get_last_player_id():
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                SELECT id FROM players ORDER BY id DESC LIMIT 1
            ''').fetchone()
