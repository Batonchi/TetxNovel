from app.items.model import *
from app.dices.model import *
# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу


class ExistCreature:

    def __init__(self, id: int, hero_name: str, history: str, friendly_degree: int, items: str, xp: int, atk: int):
        self.hero_name = hero_name
        self.history = history
        self.friendly_degree = friendly_degree
        self.items = items
        self.xp = xp
        self.atk = atk
        self.id = id

    def use_item(self, item, enemy):
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

    def cast_dice(self, dice: Dice):
        self.dice.cast_dice().do_affect(self)

    def __str__(self):
        return str({'hero_name': self.hero_name, 'history': self.history,
                    'friendly_degree': self.friendly_degree, 'items': self.items, 'xp': self.xp, 'atk': self.atk})
