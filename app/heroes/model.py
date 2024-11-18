class ExistCreature:

    def __init__(self, hero_name: str, history: str, friendly_degree: int, items: str, skills: str, id=None):
        self.hero_name = hero_name
        self.history = history
        self.friendly_degree = friendly_degree
        self.items = items
        self.skills = skills
        if id:
            self.id = id


class Enemy(ExistCreature):
    def __init__(self, exist_creature: ExistCreature, xp: int=100, atk: int=5):
        super().__init__(exist_creature.hero_name, exist_creature.history, exist_creature.friendly_degree,
                         exist_creature.items, exist_creature.skills, exist_creature.id)
        self.xp = xp
        self.default_xp = xp
        self.atk = atk


class Hero(ExistCreature):
    def __init__(self, exist_creature: ExistCreature, xp: int=100, atk: int=5):
        super().__init__(exist_creature.hero_name, exist_creature.history, exist_creature.friendly_degree,
                         exist_creature.items, exist_creature.skills, exist_creature.id)
        self.xp = xp
        self.default_xp = xp
        self.atk = atk
