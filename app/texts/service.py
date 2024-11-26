from app.texts.model import Text
from database import get_connection
from constant import *


# работа с БД таблицами
# работа с одноименной таблицей БД
class TextService:

    # функция для работы с получением списка данных по значениям аргументов в таблице
    @staticmethod
    def get_texts_by_region_id_and_hero_name(region_id: int, hero_name: int):
        with (get_connection(PATH) as conn):
            result = conn.cursor().execute('''SELECT * FROM texts WHERE region_id = ? and who_says = ?''',
                                           (region_id, hero_name)).fetchall()
            return [Text(text[1], text[2], text[3], text[4], text[0]) for text in result]

    # функция для работы с получением данных по значениям аргументов в таблице
    @staticmethod
    def get_text_by_region_id_and_hero_name(region_id: int, hero_name: int):
        with (get_connection(PATH) as conn):
            result = conn.cursor().execute('''SELECT * FROM texts WHERE region_id = ? and who_says = ?''',
                                           (region_id, hero_name)).fetchone()
            return Text(result[1], result[2], result[3], result[4], result[0])

    # функция для работы с изменением данных в таблице
    @staticmethod
    def set_text(text: Text):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''INSERT INTO texts (content, degree_of_friendly, region_id, who_says) 
            VALUES  (?, ?, ?, ?)''', (text.content, text.degree_of_friendly, text.region_id, text.who_say))
            conn.commit()

    # функция для работы с удалением данных в таблице
    @staticmethod
    def drop_text_by_id(text_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''DELETE FROM texts WHERE id = ?''', text_id)
            conn.commit()


# работа с одноименной таблицей БД
class AnswerTextService:

    # функция для работы с получением по индификатору данных в таблице
    @staticmethod
    def get_text_by_region_id(region_id: int):
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                    SELECT * FROM answwer_texts WHERE region_id = ?
                ''', region_id).fetchone()

    # функция для работы с изменением данных в таблице
    @staticmethod
    def set_text(text: Text):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO answer_texts (content, degree_of_friendly, region_id) VALUES (?, ?, ?, ?)
            ''')

    # функция для работы с удалением данных в таблице
    @staticmethod
    def drop_text_by_id(text_id: int):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
            DELETE FROM answer_texts WHERE id = ?''', text_id)
            conn.commit()

