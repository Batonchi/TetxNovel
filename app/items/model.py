from random import choice
from app.formation import deforms, format_description
from app.skills.model import *
# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу


effects = {
    'reverse_action': lambda prob: -1 if (choice([True for _ in range(round(prob * 100))]
                                          + [False for _ in range(1 - round(prob * 100))])) else 1,
    'crit-damage': crit_damage,
    'dodge': dodge,
    'stranger': stranger
}


class Item:

    def __init__(self, id: int, item_name: str, description: str, type_of_item: str):
        self.item_name = item_name
        self.description = description
        self.type_of_item = type_of_item
        self.id = id


class Weapon(Item):

    def __init__(self, id: int, item_name: str, description: str, type_of_item: str):
        super().__init__(id, item_name, description, type_of_item)
        self.description = format_description(description)
        self.status = 'Not NULL'

    def do_action_move(self):
        self.description['endurance'] -= 1
        if self.description['endurance'] == 0:
            self.status = 'must be deleted'
            return
        mul = self.description.get('mul', 1)
        atk = self.description.get('atk', 0)
        prob = self.description.get('probability', 0.1)
        crit = self.description.get('one_shoot', 1) * effects['crit-damage'](atk, mul, prob)
        rev = effects['reverse_action'](self.description.get('reverse_action', 0.5))
        return (atk + crit) * rev


class Stranger(Item):
    def __init__(self, id: int, item_name: str, description: str, type_of_item: str):
        super().__init__(id, item_name, description, type_of_item)
        self.description = format_description(description)
        self.status = 'Not NULL'

    def do_action_move(self):
        self.description['endurance'] -= 1
        if self.description['endurance'] == 0:
            self.status = 'must be deleted'
            return
        xp = self.description.get('heal', 3)
        mul = self.description.get('mul', 1)
        atk = self.description.get('atk', 0)
        prob = self.description.get('prob', 0.1)
        crit = self.description.get('osh', 1) * effects['crit-damage'](atk, mul, prob)
        rev = effects['reverse_action'](self.description.get('reverse_action', 0.5))
        return {'xp': (atk + crit) * rev * effects['stranger'](xp, atk, prob, mul, self.description.get('drop', 0.3)),
                'atk': ((atk + crit) * rev)}


class Food(Item):
    def __init__(self, id: int, item_name: str, description: str, type_of_item: str):
        super().__init__(id, item_name, description, type_of_item)
        self.description =format_description(description)
        self.status = 'Not NULL'

    def do_action_move(self):
        mul = self.description.get('mul', 1)
        xp = self.description.get('heal', 3)
        rev = effects['reverse_action'](self.description.get('reverse_action', 0.5))
        return mul * rev * effects['stranger'](xp, mul, self.description.get('drop', 0.3)) * xp

