from random import choice
from app.heroes.model import Hero, Enemy


class Item:

    def __init__(self, item_name: str, description: str, type_of_item: str, id: int=None):
        self.item_name = item_name
        self.description = description
        self.type_of_item = type_of_item
        if id:
            self.id = id


class Weapon(Item):

    def __init__(self, item_name: str, description: str, type_of_item: str, endurance: int=1, atk: int=5,
                 mul: float=0.1, id: int=None):
        super().__init__(item_name, description, type_of_item, id)
        self.atk = atk
        self.endurance = endurance
        self.effects = {
            'heal': 0,
            'one_shoot': 0,
            'reverse_action': 0,
            'drop_dice_probability': 0.01
        }
        self.mul = mul
        self.status = 'Not NULL'

    def do_action_move(self, hero, enemy):
        result_attack = self.atk * self.mul
        reverse_action_do = round(self.effects['reverse_action'] * 100)
        reverse = choice([True for _ in range(reverse_action_do)] + [False for _ in range(100 - reverse_action_do)])
        upgrade_or_decline_effect = choice(['heal', 'one_shot'])
        if reverse:
            match upgrade_or_decline_effect:
                case 'heal':
                    enemy.xp += enemy.active_dice().drop_dice() * self.effects['health']
                case 'one_shot':
                    hero.xp -= result_attack * enemy.active_dice().drop_dice() * self.effects['one_shot']
        else:
            match upgrade_or_decline_effect:
                case 'heal':
                    hero.xp += hero.active_dice().drop_dice() * self.effects['health']
                case 'one_shot':
                    enemy.xp -= result_attack * hero.active_dice().drop_dice() * self.effects['one_shot']
        self.endurance -= 1
        if self.endurance == 0:
            self.status = 'must be deleted'


class Stranger(Item):
    def __init__(self, item_name: str, description: str, type_of_item: str, endurance: int=1, mul: float=0.01, id: int=None):
        super().__init__(item_name, description, type_of_item, id)
        self.mul = mul
        self.endurance = endurance
        self.effects = {
            'health': 10,
            'one_shot': 100,
            'reverse_action': 0.01
        }

    def do_action_move(self, hero, enemy):
        choice_list = [False for _ in range(99)] + [True]
        if choice(choice_list):
            enemy.xp += self.effects['health'] * self.mul
            hero.xp -= self.effects['one_shot'] * self.mul
            self.endurance -= 1
        else:
            hero.xp += self.effects['health'] * self.mul
            enemy.xp -= self.effects['one_shot'] * self.mul
            self.endurance -= 1
        if self.endurance == 0:
            self.status = 'must be deleted'

    def lucky_or_unlucky_dice_power(self, hero: Hero, enemy: Enemy):
        local_effect = {
            'death': True,
            '1xp_for_your_person': True,
            '1xp_for_enemy': True,
            '100-pro-heal'":": True,
            'its-more-fun-together': True
        }
        this_is_you_choice_bitch = choice(list(local_effect.keys()))
        match this_is_you_choice_bitch:
            case 'death':
                hero.xp = 0
            case '1xp_for_your_person':
                hero.xp = 1
            case '100-pro-heal':
                hero.xp = hero.default_xp
            case '1xp_for_enemy':
                enemy.xp = 1
            case 'its-more-fun-together':
                enemy.xp = 0
                hero.xp = 1


class Food(Item):
    def __init__(self, item_name: str, description: str, type_of_item: str, heal_or_unheal=True, id: int=None):
        super.__init__(item_name, description, type_of_item, id)
        self.status = 'Not NULL'
        self.change_xp = description
        self.heal_or_unheal = heal_or_unheal

    def do_action_move(self, hero: Hero):
        if self.heal_or_unheal:
            hero.xp += self.change_xp
        else:
            hero.xp += self.change_xp * -1
