from app.gameSession.model import Session, Region
from database import get_connection
from constant import *
# классы для работы с БД и  функция генерации карты мира


def generate_world_map():
    with get_connection(PATH) as conn:
        cur = conn.cursor()
        query = '''SELECT * FROM regions'''
        cur.execute(query)
        rows = cur.fetchall()
        return '\n'.join(rows)


class RegionService:

    @staticmethod
    def set_region(region: Region):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO regions (region_name, hero_placed, maybe_items) VALUES (?, ?, ?)'''
            values = (region.region_name, region.hero_placed, region.maybe_items)
            cur.execute(query, values)
            conn.commit()

    @staticmethod
    def get_region_by_name(region_name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = f'SELECT * FROM regions WHERE name = {region_name}'
            cur.execute(query)
            result = cur.fetcone()
            return Region(result[1], result[2], result[3], result[0])


class SessionService:

    @staticmethod
    def set_session(session: Session):
        with get_connection(PATH) as conn:
            values = (session.player_id, session.checkpoint, session.player_puppet)
            conn.cursor().execute(f'INSERT INTO sessions (player_id, checkpoint, player_puppet) VALUES (?, ?, ?)',
                                  values)

    @staticmethod
    def get_session_by_player_id(player_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute(f'SELECT * FROM sessions WHERE player_id = {player_id}').fetchone()
            return Session(result[1], result[2], result[3], result[0])

    @staticmethod
    def get_last_session_id():
        with get_connection(PATH) as conn:
            try:
                return conn.cursor().execute(f'SELECT * FROM sessions ORDER BY id DESC LIMIT 1').fetchone()[0]
            except Exception as e:
                return 1


