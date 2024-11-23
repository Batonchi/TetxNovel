from app.skills.model import *
from app.items.model import *
# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу


class ExistCreature:

    def __init__(self, id: int, hero_name: str, history: str, friendly_degree: int, items: str, skills: str):
        self.hero_name = hero_name
        self.history = history
        self.friendly_degree = friendly_degree
        self.items = items
        self.skills = skills
        self.id = id


class Enemy(ExistCreature):
    def __init__(self, exist_creature: ExistCreature, xp: int = 1000, atk: int = 15):
        super().__init__(exist_creature.id, exist_creature.hero_name, exist_creature.history,
                         exist_creature.friendly_degree,
                         exist_creature.items, exist_creature.skills)
        self.xp = xp
        self.default_xp = xp
        self.atk = atk
        self.dices = []

    def use_item(self, item, hero=None):
        use = item.do_action_move()
        xp = round(use.get('xp', 0))
        atk = round(use.get('atk', 0))
        self.xp += xp
        if atk > 0:
            self.do_attack_after_use_item(atk, hero)
        else:
            self.xp -= atk

    def take_damage(self, damage: int):
        self.xp -= damage

    def do_attack_after_use_item(self, atk, hero):
        hero.xp -= self.atk + atk

    def do_attack(self, hero):
        hero.xp += self.atk


class Hero(ExistCreature):
    def __init__(self, exist_creature: ExistCreature, xp: int=1000, atk: int=15):
        super().__init__(exist_creature.id, exist_creature.hero_name, exist_creature.history,
                         exist_creature.friendly_degree,
                         exist_creature.items, exist_creature.skills)
        self.xp = xp
        self.default_xp = xp
        self.atk = atk
        self.dices = []

    def use_item(self, item, enemy=None):
        use = item.do_action_move()
        xp = round(use.get('xp', 0))
        atk = round(use.get('atk', 0))
        self.xp += xp
        if atk > 0:
            self.do_attack_after_use_item(atk, enemy)
        else:
            self.xp -= atk

    def take_damage(self, damage: int):
        self.xp -= damage

    def do_attack_after_use_item(self, atk, enemy):
        enemy.xp -= self.atk + atk

    def do_attack(self, enemy):
        enemy.xp += self.atk
