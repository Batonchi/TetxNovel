from app.dices.model import Dice, Face
from database import get_connection
from constant import PATH
from random import choices, randint
# класс работающий с БД с таблицей dices


# класс для работы с одноименной таблицей БД
class DiceService:
    # функция для работы с заполнением таблицы
    @staticmethod
    def set_dice(dice: Dice):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO dices (name_of_dice, num_of_faces, description, faces) VALUES (?, ?, ?, ?)'''
            values = (dice.name_of_dice, dice.num_of_faces, dice.description, dice.faces)
            cur.execute(query, values)
            conn.commit()

    # функция для работы с получением данных из таблицы
    @staticmethod
    def get_dice_by_name(name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''SELECT * FROM dices WHERE name_of_dice = ?'''
            value = (name,)
            cur.execute(query, value)
            result = cur.fetchone()
            if result:
                return Dice(result[1], result[2], result[3], result[4], result[0])

    # функция для работы с удалением данных из таблицы
    @staticmethod
    def drop_dice(name: str):
        with get_connection() as conn:
            cur = conn.cursor()
            query = '''DELETE FROM dices WHERE name_of_dice = ?'''
            value = (name,)
            cur.execute(query, value)
            conn.commit()

    # функция для генерации игровой кости
    @staticmethod
    def generate_dice(name: str, description: str, faces: list=None):
        if faces is None:
            faces = FaceService.get_faces()
        res = choices(faces, k=randint(1, 5))
        return Dice(name, len(res), description, ' '.join(res))


# класс для работы с одноименной таблицей БД
class FaceService:
    # функция для работы с заполнением таблицы
    @staticmethod
    def set_face(face: Face):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO faces (face_name, description) VALUES (?, ?)'''
            values = (face.face_name, face.description)
            cur.execute(query, values)
            conn.commit()

    # функция для работы с получением данных из таблицы
    @staticmethod
    def get_face_by_name(name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''SELECT * FROM faces WHERE name_of_face = ?'''
            value = (name,)
            cur.execute(query, value)
            result = cur.fetchone()
            return Face(result[1], result[2], result[0])

    # функция для работы с получением данных из таблицы
    @staticmethod
    def get_faces():
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''SELECT * FROM faces'''
            cur.execute(query)
            result = cur.fetchall()
            return [Face(el[1], el[2], el[0]) for el in result]

    # функция для работы с удалением данных из таблицы
    @staticmethod
    def drop_face_by_name(name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''DELETE FROM faces WHERE name_of_face = ?'''
            value = (name,)
            cur.execute(query, value)
            conn.commit()