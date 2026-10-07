from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategy(Exception):
    ...


class BattleStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._strat = ""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._strat = "Normal"

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(f"{creature.attack()}")
        else:
            raise InvalidStrategy(f"Invalid Creature {creature.get_name()} "
                                  " for this normal strategy")

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._strat = "Aggresive"

    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(f"{creature.transform()}")
            print(f"{creature.attack()}")
            print(f"{creature.revert()}")
        else:
            raise InvalidStrategy(f"Invalid Creature '{creature.get_name()}'"
                                  " for this aggresive strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._strat = "Defensive"

    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(f"{creature.attack()}")
            print(f"{creature.heal()}")
        else:
            raise InvalidStrategy(f"Invalid Creature '{creature.get_name()}'"
                                  " for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
