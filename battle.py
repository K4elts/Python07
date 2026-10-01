from ex0 import CreatureFactory, FlameFactory, AquaFactory


def testing_factory(monster_factory: CreatureFactory) -> None:
    print("Testing factory")
    base_monster = monster_factory.create_base()
    print(base_monster.describe())
    print(base_monster.attack())
    evolved_monster = monster_factory.create_evolved()
    print(evolved_monster.describe())
    print(evolved_monster.attack())
    print()


def testing_battle(
        monster_fac_1: CreatureFactory,
        monster_fac_2: CreatureFactory
) -> None:
    print("Testing battle")
    monster_1 = monster_fac_1.create_base()
    monster_2 = monster_fac_2.create_base()
    print(monster_1.describe())
    print("vs")
    print(monster_2.describe())
    print(" fight!")
    print(monster_1.attack())
    print(monster_2.attack())


if __name__ == "__main__":
    fire_factory = FlameFactory()
    testing_factory(fire_factory)
    water_factory = AquaFactory()
    testing_factory(water_factory)
    print()
    testing_battle(fire_factory, water_factory)
