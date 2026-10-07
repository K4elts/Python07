from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    InvalidStrategy,
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy)


def fight(
        fact_1: CreatureFactory,
        strat_1: BattleStrategy,
        fact_2: CreatureFactory,
        strat_2: BattleStrategy
) -> None:
    monster_1 = fact_1.create_base()
    monster_2 = fact_2.create_base()
    print()
    print("* Battle *")
    print(f"{monster_1.describe()}")
    print(" vs")
    print(f"{monster_2.describe()}")
    print(" now fight!")
    strat_1.act(monster_1)
    strat_2.act(monster_2)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:
        for i, (fact_1, strat_1) in enumerate(opponents):
            for fact_2, strat_2 in opponents[i + 1:]:
                fight(fact_1, strat_1, fact_2, strat_2)
    except InvalidStrategy as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    flame_fact = FlameFactory()
    heal_fact = HealingCreatureFactory()
    aqua_fact = AquaFactory()
    shift_fact = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    agg_strat = AggressiveStrategy()
    def_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    battle([(flame_fact, normal_strat), (heal_fact, def_strat)])
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    battle([(flame_fact, agg_strat), (heal_fact, def_strat)])
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggresive) ]")
    print("*** Tournament ***")
    print("3 opponens involved")
    battle([(aqua_fact, normal_strat), (heal_fact, def_strat),
           (shift_fact, agg_strat)])
