from random import randint, choice

import constants
from service.persons import Paladin, Warrior
from service.things import Helm, Ring, Shield, Sword, Boots, Staff

THING_CLASSES = [
    Helm,
    Ring,
    Shield,
    Sword,
    Boots,
    Staff
]

PERSON_CLASSES = [
    Paladin,
    Warrior
]

persons = []

for _ in range(10):
    things = []
    for _ in range(randint(1, 4)):
        things.append(choice(THING_CLASSES)())
    persons.append(choice(PERSON_CLASSES)(choice(constants.NAMES), things))


while len(persons) != 1:
    attacker = choice(persons)
    defender = choice(persons)

    while defender == attacker:
        defender = choice(persons)

    print(f'\nАтакует {attacker.name}. Защищается {defender.name}.')
    damage = defender.get_damage(attacker.attack_damage())
    print(f'{defender.name} получает урон {round(damage, 2)}.')

    if defender.hit_points > 0:
          print(f'У {defender.name} осталось {round(defender.hit_points, 2)} HP')
    elif defender.hit_points <= 0:
        print(f'{defender.name} погиб.')
        persons.remove(defender)


print(f'\nПобедитель - {persons[0].name}')
