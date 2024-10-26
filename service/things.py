class Thing:
    """Базовый класс вещи."""

    def __init__(
            self,
            name: str,
            defence: float,
            attack: float,
            hit_points: float
    ):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hit_points = hit_points


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