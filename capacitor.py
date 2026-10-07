from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing_creature() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base_monster = HealingCreatureFactory().create_base()
    print(f"{base_monster.describe()}")
    print(f"{base_monster.attack()}")
    if isinstance(base_monster, HealCapability):
        print(f"{base_monster.heal()}")
    print(" evolved:")
    evolved_monster = HealingCreatureFactory().create_evolved()
    print(f"{evolved_monster.describe()}")
    print(f"{evolved_monster.attack()}")
    if isinstance(evolved_monster, HealCapability):
        print(f"{evolved_monster.heal()}")


def test_transform_creature() -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base_monster = TransformCreatureFactory().create_base()
    print(f"{base_monster.describe()}")
    print(f"{base_monster.attack()}")
    if isinstance(base_monster, TransformCapability):
        print(f"{base_monster.transform()}")
        print(f"{base_monster.attack()}")
        print(f"{base_monster.revert()}")
    print(" evolved:")
    evolved_monster = TransformCreatureFactory().create_evolved()
    print(f"{evolved_monster.describe()}")
    print(f"{evolved_monster.attack()}")
    if isinstance(evolved_monster, TransformCapability):
        print(f"{evolved_monster.transform()}")
        print(f"{evolved_monster.attack()}")
        print(f"{evolved_monster.revert()}")


if __name__ == "__main__":
    test_healing_creature()
    print()
    test_transform_creature()
