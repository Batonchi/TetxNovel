from model import Session, Region
from app.database import get_connection
from app.constant import *


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
            query = (f'INSERT INTO regions'
                     f' (region_name, description, hero_placed, maybe_items) VALUES (%s, %s, %s, %s)')
            values = (region.region_name, region.description, region.hero_placed, region.maybe_items)
            cur.execute(query, values)
            conn.commit()

    @staticmethod
    def get_region_by_name(region_name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = f'SELECT * FROM regions WHERE name = {region_name}'
            cur.execute(query)
            return cur.fetcone()


class SessionService:

    @staticmethod
    def set_session(session: Session):
        with get_connection(PATH) as conn:
            values = (session.player_id, session.world_map, session.placement, session.checkpoint, session.items,
                      session.the_player_puppet)
            conn.cursor().execute(f'INSERT INTO sessions VALUES (%s, %s, %s, %s, %s, %s)', values)

    @staticmethod
    def get_session_by_player_id(session_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute(f'SELECT * FROM sessions WHERE id = {session_id}').fetchall()


