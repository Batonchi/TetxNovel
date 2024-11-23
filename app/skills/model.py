from random import choice
from app.dices.model import Dice


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