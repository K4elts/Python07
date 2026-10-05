from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        else:
            return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastrting morph strike!"
        else:
            return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."
