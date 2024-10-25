from random import randint, choice

BASE_DEFENCE = 0.1
BASE_ATTACK = 10
BASE_HP = 100

NAME = [
    'Итан',
    'Эйден',
    'Лиам',
    'Оливер',
    'Яшма',
    'Феликс',
    'Орион',
    'Рис',
    'Морн',
    'Ноач',
    'Амелия',
    'Эвелин',
    'София',
    'Ава',
    'Миа',
    'Луна',
    'Аврора',
    'Ирис',
    'Серафина',
    'Вилоу'
]

class Thing:
    """Базовый класс вещи."""

    def __init__(self, name: str, defence: float, attack: float, hp: float):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp

class Helm(Thing):
    """Класс вещи - Шлем."""

    def __init__(self):
        super().__init__('Helm', 0.05, 0, 10)

class Ring(Thing):
    """Класс вещи - Кольцо."""

    def __init__(self):
        super().__init__('Ring', 0.07, 5, 10)

class Sword(Thing):
    """Класс вещи - Меч."""

    def __init__(self):
        super().__init__('Sword', 0, 0, 30)

class Shield(Thing):
    """Класс вещи - Щит."""

    def __init__(self):
        super().__init__('Shield', 0.09, 2, 0)

class Boots(Thing):
    def __init__(self):
        super().__init__('Boots', 0.05, 0, 15)

class Staff(Thing):
    """Класс вещи - Посох."""

    def __init__(self):
        super().__init__('Helm', 0, 15, 20)


class Person:
    """Базовый класс персонажа."""

    def __init__(
            self,
            name: str,
            things: list[Thing],
            defence: float = BASE_DEFENCE,
            attack: float = BASE_ATTACK,
            hit_point: float = BASE_HP,
        ):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hit_point = hit_point
        self.things = things
        self.things_name = []
        self.set_things()

    def set_things(self) -> None:
        """Добавляет предметы персонажу."""
        for thing in self.things:
            self.defence += thing.defence
            self.attack += thing.attack
            self.hit_point += thing.hp
            self.things_name.append(thing.name)


    def get_damage(self, damage: float) -> float:
        """Расчет полученного урона."""
        damage_fact = damage - (damage * self.defence)
        self.hit_point -= damage_fact
        return damage_fact


    def attack_damage(self) -> float:
        """Урона, который наносит персонаж."""
        return self.attack


class Paladin(Person):
    """Класс персонажа - Палладин."""
    def __init__(self, name, things):
        super().__init__(name, things)
        self.defence *= 2


class Warrior(Person):
    """Класс персонажа - Воин."""
    def __init__(self, name, things):
        super().__init__(name, things)
        self.attack *= 2


persons = []
for _ in range(10):
    things = []
    for _ in range(randint(1, 4)):
        things.append(choice([Helm(), Ring(), Sword(), Shield(), Boots(), Staff()]))
    persons.append(choice([Paladin(choice(NAME), things=things), Warrior(choice(NAME), things=things)]))


while len(persons) != 1:
    attacker = choice(persons)
    defender = choice(persons)

    while defender == attacker:
        defender = choice(persons)

    print(f'\nАтакует {attacker.name}. Защищается {defender.name}.')
    damage = defender.get_damage(attacker.attack_damage())
    print(f'{defender.name} получает урон {round(damage, 2)}.'
          f'У {defender.name} осталось {round(defender.hit_point, 2)} HP')

    if defender.hit_point <= 0:
        print(f'{defender.name} died.')
        persons.remove(defender)


print(f'Победитель - {persons[0].name}')
