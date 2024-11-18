from random import choice


class Dice:

    def __init__(self, name_of_dice, num_of_faces: int, description: str, faces: str, id=None):
        self.name_of_dice = name_of_dice
        self.num_of_faces = num_of_faces
        self.description = description
        self.faces = faces
        if id:
            self.id = id

    def cast_dice(self):
        return choice(self.faces)

    def __str__(self):
        return self.description


class Face:

    def __init__(self, face_name: str, description: str, effects: dict = None, id=None):
        self.face_name = face_name
        self.description = {}
        for el in description.split('\n'):
            astr = el.split(' = ')
            self.description[astr[0]] = astr[1]
        if id:
            self.id = id
        if effects:
            self.effects = effects

    def __str__(self):
        return self.description


