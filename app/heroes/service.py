from app.heroes.model import ExistCreature
from constant import *
from database import get_connection
#  смотрите названия методов: добавляет, удаляет и создает сущесвто


class ExistCreatureService:
    @staticmethod
    def set_creature(exist_creature: ExistCreature):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''INSERT INTO heroes VALUES (?, ?, ?, ?, ?)''',
                                  (exist_creature.hero_name, exist_creature.history, exist_creature.items,
                                   exist_creature.xp, exist_creature.atk))
            conn.commit()

    @staticmethod
    def get_first_creature():
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM heroes ORDER BY id ASC LIMIT 1''').fetchone()
            return ExistCreature(result[1], result[2], result[3], result[4], result[5], result[0])

    @staticmethod
    def drop_creature_by_name(name: str):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''DELETE FROM heroes WHERE name = ?''', name)
            conn.commit()
