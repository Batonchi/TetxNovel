from random import choice
from app.formation import deforms, format_description
# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу


class Dice:

    def __init__(self, id: int, name_of_dice, num_of_faces: int, description: str, faces: str):
        self.id = id
        self.name_of_dice = name_of_dice
        self.num_of_faces = num_of_faces
        self.description = description
        self.faces = faces

    def cast_dice(self):
        face = choice(self.faces)
        return Face(face.id, face.face_name, format_description(face.description))

    def __str__(self):
        return self.description


class Face:

    def __init__(self, id: int, face_name: str, description: str):
        self.id = id
        self.face_name = face_name
        self.description = description

    def __str__(self):
        return self.description


