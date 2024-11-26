from app.heroes.model import ExistCreature
from constant import *
from database import get_connection
#  смотрите названия методов: добавляет, удаляет и создает сущесвто


# работа с одноименной таблицей БД
class ExistCreatureService:
    # функция для работы с изменениеми в таблице
    @staticmethod
    def set_creature(exist_creature: ExistCreature):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''INSERT INTO heroes (hero_name, history, friendly_degree) VALUES (?, ?, ?)''',
                                  (exist_creature.hero_name, exist_creature.history, exist_creature.friendly_degree))
            conn.commit()

    # функция для работы с  стандартными изменениями в таблицеизменениеми в таблице
    @staticmethod
    def set_default_creature(exist_creature: ExistCreature):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''INSERT INTO heroes (hero_name, history, friendly_degree, items, atk, xp)
             VALUES (?, ?, ?, ?, ?, ?)''',
                                  (exist_creature.hero_name, exist_creature.history, exist_creature.friendly_degree,
                                   exist_creature.items, exist_creature.atk, exist_creature.xp))
            conn.commit()

    # функция для работы с  получением данных из таблицы
    @staticmethod
    def get_first_creature():
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM heroes ORDER BY id ASC LIMIT 1''').fetchone()
            return ExistCreature(result[1], result[2], result[3], result[4], result[5], result[6], result[0])

    # функция для получения создания по индефикатору
    @staticmethod
    def get_creature_by_id(hero_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute(f'''SELECT * FROM heroes WHERE id = {hero_id}''').fetchone()
            return ExistCreature(result[1], result[2], result[3], result[4], result[5], result[6], result[0])

    # функция для получения создания по имени
    @staticmethod
    def get_creature_by_name(name: str):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM heroes WHERE hero_name = ?''', (name,)).fetchone()
            return ExistCreature(result[1], result[2], result[3], result[4], result[5], result[6], result[0])

    # функция для удаления создания по имени
    @staticmethod
    def drop_creature_by_name(name: str):
        with get_connection(PATH) as conn:
            conn.cursor().execute(
                '''DELETE FROM heroes WHERE name = ?''', (name,))
            conn.commit()
