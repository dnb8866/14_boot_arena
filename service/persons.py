import constants
from service.things import Thing


class Person:
    """Базовый класс персонажа."""

    def __init__(
            self,
            name: str,
            things: list[Thing],
            defence: float = constants.BASE_DEFENCE,
            attack: float = constants.BASE_ATTACK,
            hit_points: float = constants.BASE_HP,
    ):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hit_points = hit_points
        self.things = things
        self.things_name = []
        self.set_things()

    def set_things(self) -> None:
        """Добавляет предметы персонажу."""
        for thing in self.things:
            self.defence += thing.defence
            self.attack += thing.attack
            self.hit_points += thing.hit_points
            self.things_name.append(thing.name)

    def get_damage(self, damage: float) -> float:
        """Расчет полученного урона."""
        damage_fact = damage - (damage * self.defence)
        self.hit_points -= damage_fact
        return damage_fact

    def attack_damage(self) -> float:
        """Урона, который наносит персонаж."""
        return self.attack


class Paladin(Person):
    """Класс персонажа - Палладин."""

    def __init__(self, name: str, things: list[Thing]):
        super().__init__(name, things)
        self.defence *= 2


class Warrior(Person):
    """Класс персонажа - Воин."""

    def __init__(self, name: str, things: list[Thing]):
        super().__init__(name, things)
        self.attack *= 2