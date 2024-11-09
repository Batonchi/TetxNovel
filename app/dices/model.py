class Dice:

    def __init__(self, name_of_dice, num_of_faces: int, description: str, id=None):
        self.name_of_dice = name_of_dice
        self.num_of_dices = num_of_faces
        self.description = description
        if id:
            self.id = id


class Face:

    def __init__(self, face_name: str, description: str, id=None):
        self.face_name = face_name
        self.description = description
        if id:
            self.id = id