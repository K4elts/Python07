from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        super().__init__()
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self._name} uses Water Pump!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"
