from random import choice
from formation import format_description
# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу


class Dice:

    def __init__(self, name_of_dice, num_of_faces: int, description: str, faces: str, dice_id: int = None):
        if dice_id:
            self.dice_id = dice_id
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

    def __init__(self, face_name: str, description: str, face_id: int = None):
        if face_id:
            self.face_id = face_id
        self.face_name = face_name
        self.description = description

    def __str__(self):
        return self.description

    def face_affect(self, creature):
        desc = format_description(self.description)
        prob = desc['reverse_action']
        if desc['value'] >= 5 and 'ступень ада' in self.face_name:
            if choice([True for _ in range(round(prob * 100))] + [Face for _ in range(1 - round(prob * 100))]):
                creature.xp -= 20
            else:
                creature.atk += 5
                creature.xp -= 5
        elif desc['value'] < 5 and 'ступень ада' in self.face_name:

            if choice([True for _ in range(round(prob * 100))] + [Face for _ in range(1 - round(prob * 100))]):
                creature.atk -= 5
            else:
                creature.atk -= 1
                creature.xp += 10
        elif desc['value'] < 5 and 'сторона ада' in self.face_name:
            if choice([True for _ in range(round(prob * 100))] + [Face for _ in range(1 - round(prob * 100))]):
                creature.atk += 5
            else:
                creature.atk += 1
                creature.xp += 7
        elif desc['value'] >=5 and 'сторона ада' in self.face_name:
            if choice([True for _ in range(round(prob * 100))]):
                creature.xp -= 200

