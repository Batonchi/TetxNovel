from app.heroes.model import ExistCreature
from app.constant import *
from app.database import get_connection


class ExistCreatureService:
    @staticmethod
    def set_creature(exist_creature: ExistCreature):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO heroes VALUES (%s, %s, %s, %s)
            ''', (exist_creature.hero_name, exist_creature.history, exist_creature.items, exist_creature.skills))
            conn.commit()

    @staticmethod
    def get_creature_by_name(name: str):
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                SELECT * FROM heroes WHERE name = %s
            ''', name).fetchone()

    @staticmethod
    def drop_creature_by_name(name: str):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''
                    DELETE FROM heroes WHERE name = %s
                ''', name)
