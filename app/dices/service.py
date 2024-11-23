from app.dices.model import Dice, Face
from app.database import get_connection
from app.constant import PATH
from random import choices, randint


class DiceService:
    @staticmethod
    def set_dice(dice: Dice):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO dices (id, name_of_dice, num_of_faces, description, faces) VALUES (?, ?, ?, ?, ?)'''
            values = (dice.id, dice.name_of_dice, dice.num_of_faces, dice.description, dice.faces)
            cur.execute(query, values)
            conn.commit()

    @staticmethod
    def get_dice_by_name(name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''SELECT * FROM dices WHERE name_of_dice = ?'''
            value = name
            cur.execute(query, value)
            result = cur.fetchone()
            if result:
                return Dice(result[1], result[2], result[3], result[4], result[0])

    @staticmethod
    def drop_dice(name: str):
        with get_connection() as conn:
            cur = conn.cursor()
            query = '''DELETE FROM dices WHERE name_of_dice = ?'''
            value = name
            cur.execute(query, value)
            conn.commit()

    @staticmethod
    def generate_dice(name: str, description: str, faces: list=None):
        if faces is None:
            faces = FaceService.get_faces()
        res = choices(faces, k=randint(1, 5))
        return Dice(name, len(res), description, ' '.join(res))


class FaceService:

    @staticmethod
    def set_face(face: Face):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''INSERT INTO faces (id, face_name, description) VALUES (?, ?, ?)'''
            values = (face.id, face.face_name, face.description)
            cur.execute(query, values)
            conn.commit()

    @staticmethod
    def get_face_by_name(name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''SELECT * FROM faces WHERE name_of_face = ?'''
            value = name
            cur.execute(query, value)
            result = cur.fetchone()
            return result

    @staticmethod
    def get_faces():
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''SELECT * FROM faces'''
            cur.execute(query)
            result = cur.fetchall()
            return result

    @staticmethod
    def drop_face(name: str):
        with get_connection(PATH) as conn:
            cur = conn.cursor()
            query = '''DELETE FROM faces WHERE name_of_face = ?'''
            value = name
            cur.execute(query, value)
            conn.commit()