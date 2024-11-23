from app.players.model import Player
from app.constant import *
from app.database import get_connection


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
    def drop_player_by_id(player_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''DELETE FROM players WHERE id = ?'''
            , player_id)
            conn.commit()
