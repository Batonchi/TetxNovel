from app.texts.model import Text
from app.database import get_connection
from app.constant import *

# работа с БД таблицами
class TextService:

    @staticmethod
    def get_text_by_region_id(region_id: int):
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                SELECT * FROM texts WHERE region_id = ?
            ''', region_id).fetchone()

    @staticmethod
    def set_text(text: Text):
        pass


class AnswerTextService:

    @staticmethod
    def get_text_by_region_id(region_id: int):
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                    SELECT * FROM answwer_texts WHERE region_id = ?
                ''', region_id).fetchone()

    def set_text(self, text: Text):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO answer_texts (id, content, degree_of_friendly, region_id) VALUES (?, ?, ?, ?, ?)
            ''')

