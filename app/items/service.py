from app.items.model import Item
from app.constant import *
from app.database import get_connection


class ItemService:

    @staticmethod
    def set_item(item: Item):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
                INSERT INTO items (id, item_name, description, type_of_item) VALUES (?, ?, ?, ?)
            ''', (item.id, item.item_name, item.description, item.type_of_item))
            conn.commit()

    @staticmethod
    def get_item_by_name(name: str):
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                SELECT * FROM items WHERE name = ?
            ''', name).fetchone()

    @staticmethod
    def get_all_items():
        with get_connection(PATH) as conn:
            return conn.cursor().execute('''
                SELECT * FROM items
            ''').fetchall()

    @staticmethod
    def drop_item_by_name(name: str):
        with get_connection(PATH) as conn:
            conn.cursor().execute('''
            DELETE FROM items WHERE name = ?
            ''', name)
            conn.commit()