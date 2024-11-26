from app.gameSession.model import Session, Region
from database import get_connection
from constant import *
# классы для работы с БД и  функция генерации карты мира


# класс для работы с одноименной таблицей из БД
class RegionService:
    # функция для работы с изменением данных в таблице

    @staticmethod
    def set_region(region: Region):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO regions (region_name, heroes_placed) VALUES (?, ?)'''
            values = (region.region_name, region.heroes_placed)
            cur.execute(query, values)
            conn.commit()

    # функция для работы с основными изменением данных в таблице
    @staticmethod
    def set_default_region(region: Region):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO regions (region_name, hero_placed, maybe_items) VALUES (?, ?, ?)'''
            values = (region.region_name, region.hero_placed, region.maybe_items)
            cur.execute(query, values)
            conn.commit()

    # функция для работы с получением данных по имени региона в таблице
    @staticmethod
    def get_region_by_name(region_name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = f'SELECT * FROM regions WHERE name = ?'
            values = (region_name,)
            cur.execute(query, values)
            result = cur.fetcone()
            return Region(result[1], result[2], result[3], result[0])

    # функция для работы с получением по индефикатору данных в таблице
    @staticmethod
    def get_region_by_id(region_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM regions WHERE id = ?''', (region_id,)).fetchone()
            return Region(result[1], result[2], result[3], result[0])


# класс для работы с одноименной таблицей БД
class SessionService:
    # функция для работы с изменением данных в таблице

    @staticmethod
    def set_session(session: Session):
        with get_connection(PATH) as conn:
            values = (session.player_id, session.checkpoint, session.player_puppet)
            conn.cursor().execute(f'INSERT INTO sessions (player_id, checkpoint, player_puppet) VALUES (?, ?, ?)',
                                  values)

    # функция для работы с прлучением по индификатору игрока данных в таблице
    @staticmethod
    def get_session_by_player_id(player_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM sessions WHERE player_id = ?''', (player_id,)).fetchone()
            return Session(result[1], result[2], result[3], result[0])

    # функция для работы с получения по индификатору сессии данных в таблице
    @staticmethod
    def get_session_by_id(session_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM sessions WHERE id = ?''', (session_id,)).fetchone()
            return Session(result[1], result[2], result[3], result[0])

    # функция для работы с обновлением данных в таблице
    @staticmethod
    def update_checkpoint(checkpoint: int, session_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''UPDATE sessions SET checkpoint = ? WHERE id = ?''', (checkpoint + 1, session_id))
            conn.commit()


