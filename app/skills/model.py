


class Skill:

    def __init__(self, skill_name: str, type_of_skill: str, description: str, id=None):
        self.skill_name = skill_name
        self.type_of_skill = type_of_skill
        self.description = description
        if id:
            self.id = id


class Heal(Skill):
    def __init__(self, skill_name: str, type_of_skill: str, description: str, heal_xp: int = 3, id=None):
        super().__init__(skill_name, type_of_skill, description, id)
        self.heal_xp = heal_xp

    def heal_xp(self, creature):
        creature.xp += self.heal_xp


class OneShooter(Skill):
    def __init__(self, skill_name: str, type_of_skill: str, description: str, atk: int=10, id=None):
        super().__init__(skill_name, type_of_skill, description, id)
        self.critDMG = atk

    def return_crit_damage(self, creature):
        pass




class FriendlyFire(Skill):
    pass


class BePrettyLittleDogBitch(Skill):
    pass


class Dodge(Skill):
    pass

class Stranger(Skill):
    pass

class PowerDamage(Skill):
    pass

class ReverseAction(Skill):
    pass


class DecreaseDamageAEnemy(Skill):
    pass


class TakeDamage(Skill):
    pass


class MakeDamage(Skill):
    pass