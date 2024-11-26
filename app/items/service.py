from app.items.model import *
from constant import *
from database import get_connection


# буквально функция проверки типов
def check_type_item(item: list):
    if item[3] == 'weapon':
        return Weapon(item[1], item[2], item[3], item[0])
    elif item[3] == 'food':
        return Food(item[1], item[2], item[3], item[0])
    elif item[3] == 'stranger':
        return Stranger(item[1], item[2], item[3], item[0])
    return Item(item[1], item[2], item[3], item[0])


# класс работающий с БД с таблицей items
class ItemService:

    # функция для работы с изменением данных в таблице
    @staticmethod
    def set_item(item: Item):
        with get_connection(PATH) as conn:
            print(PATH)
            conn.cursor().execute('''
                INSERT INTO items (item_name, description, type_of_item) VALUES (?, ?, ?)
            ''', (item.item_name, item.description, item.type_of_item))
            conn.commit()

    # функция для работы с получением по имени данных в таблице
    @staticmethod
    def get_item_by_name(name: str):
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM items WHERE name = ?''', name).fetchone()
            return check_type_item(result)

    # функция для работы с получением всех данных в таблице
    @staticmethod
    def get_all_items():
        with get_connection(PATH) as conn:
            result = conn.cursor().execute('''SELECT * FROM items''').fetchall()
            return [check_type_item(el) for el in result]

    # # функция для работы с удалением данных в таблице
    @staticmethod
    def drop_item_by_name(name: str):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
            DELETE FROM items WHERE name = ?
            ''', name)
            conn.commit()