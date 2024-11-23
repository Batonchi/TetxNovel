from random import choice
from app.formation import deforms, format_description
from app.dices.model import *

# В файле описаны модели таблиц из БД которые получаются и отправляются по запросу


class Item:

    def __init__(self, id: int, item_name: str, description: str, type_of_item: str):
        self.item_name = item_name
        self.description = description
        self.type_of_item = type_of_item
        self.id = id

# класс оружия, реализующего доп. урон
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


# класс странный, просто класс, п.с. здесь все придумано из пальца как и этот класс - полная анархия))
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

# класс еды - лечит, иногда калечит
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


# как и сказано странная функция
def stranger(xp: int, atk: int, prob: float, mul: float, drop: float):
    mul += xp * atk - (prob * drop)
    random_list = ([True for _ in range(round(drop * 100))]
                   + [False for _ in range(1 - round(drop * 100))])
    if choice(random_list):
        mul += 1
    return mul


# возврат атаки, с которой произойдет удар
def crit_damage(atk: int, mul: float, prob: float):
    if choice([True for _ in range(round(prob * 100))] + [True for _ in range(1 - round(prob * 100))]):
        return atk * mul
    else:
        return atk * -1 * mul


# Функция, которая возвращаеть возможность уклонения
def dodge(dodge_probability, creature):
    result = creature.dices[0].cast_dice()
    if int(result.description['value']) >= 5:
        dodge_probability *= 5
    return choice([True for _ in range(round(dodge_probability * 100))] +
                  [False for _ in range(round(100 - dodge_probability * 100))])


# понижение урона проивника
def decrease_enemy_damage(enemy, mul: float, prob: float):
    if choice([True for _ in range(round(prob * 100))] +
                  [False for _ in range(round(100 - prob * 100))]):
        enemy.atk *= mul


# Существо наносит вред себе функция для странных действий
def self_harm(creature, mul: float, prob: float):
    if choice([True for _ in range(round(prob * 100))] +
                  [False for _ in range(round(100 - prob * 100))]):
        creature.atk *= mul
        creature.xp -= mul * creature.atk


effects = {
    'reverse_action': lambda prob: -1 if (choice([True for _ in range(round(prob * 100))]
                                          + [False for _ in range(1 - round(prob * 100))])) else 1,
    'crit-damage': crit_damage,
    'dodge': dodge,
    'stranger': stranger
}
