

BASE_DEFENCE = 0.1
BASE_ATTACK = 10
BASE_HP = 100


class Thing:
    def __init__(self, name, defence, attack, hp):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp

class Helm(Thing):
    def __init__(self):
        super().__init__('Helm', 0.05, 0, 10)

class Ring(Thing):
    def __init__(self):
        super().__init__('Ring', 0.07, 5, 10)

class Sword(Thing):
    def __init__(self):
        super().__init__('Sword', 0, 0, 30)

class Shield(Thing):
    def __init__(self):
        super().__init__('Shield', 0.09, 2, 0)

class Boots(Thing):
    def __init__(self):
        super().__init__('Boots', 0.05, 0, 15)

class Staff(Thing):
    def __init__(self):
        super().__init__('Helm', 0, 15, 20)


class Person:
    def __init__(
            self,
            name,
            things,
            base_defence=BASE_DEFENCE,
            base_attack=BASE_ATTACK,
            base_hp=BASE_HP,
        ):
        self.name = name
        self.base_defence = base_defence
        self.base_attack = base_attack
        self.base_hp = base_hp
        self.things = things
        self.things_name = []
        self.set_things()

    def set_things(self):
        for thing in self.things:
            self.base_defence += thing.defence
            self.base_attack += thing.attack
            self.base_hp += thing.hp
            self.things_name.append(thing.name)


    def get_damage(self, damage):
        self.base_hp -= damage - (damage * self.base_defence)


    def attack_damage(self):
        return self.base_attack

class Paladin(Person):
    def __init__(self, name, base_defence, base_attack, base_hp, things):
        super().__init__(name, base_defence, base_attack, base_hp, things)
        self.base_hp *= 2
        self.base_defence *= 2


class Warior(Person):
    def __init__(self, name, base_defence, base_attack, base_hp, things):
        super().__init__(name, base_defence, base_attack, base_hp, things)
        self.base_attack *= 2
