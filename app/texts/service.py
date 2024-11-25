from app.texts.model import Text
from database import get_connection
from constant import *


# работа с БД таблицами
class TextService:

    @staticmethod
    def get_text_by_region_id(region_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM texts WHERE region_id = ?''', region_id).fetchone()
            return Text(result[1], result[2], result[3], result[4], result[0])

    @staticmethod
    def set_text(text: Text):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''INSERT INTO texts (content, degree_of_friendly, region_id, who_says) 
            VALUES  (?, ?, ?, ?)''', (text.content, text.degree_of_friendly, text.region_id, text.who_say))
            conn.commit()

    @staticmethod
    def drop_text_by_id(text_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''DELETE FROM texts WHERE id = ?''', text_id)
            conn.commit()


class AnswerTextService:

    @staticmethod
    def get_text_by_region_id(region_id: int):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM texts WHERE region_id = ?''', region_id).fetchone()
            return Text(result[1], result[2], result[3], result[4], result[0])

    @staticmethod
    def set_text(text: Text):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO answer_texts (content, degree_of_friendly, region_id) VALUES (?, ?, ?, ?)
            ''')

    @staticmethod
    def drop_text_by_id(text_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
            DELETE FROM answer_texts WHERE id = ?''', text_id)
            conn.commit()

