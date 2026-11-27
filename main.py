from scene import World
from agent import Actor
from simulator import Simulator


def test():
    sim = Simulator()

    farmland = World("Myers Farm", "test.csv")
    player1 = Actor("hugright")
    farmland.add_player(player1)

    sim.add_world(farmland)
    sim.add_actor(player1)

    print(f"World Start: move count {sim.move_count}")
    sim.print_world(farmland)
    print()

    print(f"World Start: move count {sim.move_count + 1}")
    sim.sim_step(farmland, player1)
    sim.print_world(farmland)
    print()

    print(f"World Start: move count {sim.move_count + 1}")
    sim.sim_step(farmland, player1)
    sim.print_world(farmland)
    print()

    print(f"World Start: move count {sim.move_count + 1}")
    sim.sim_step(farmland, player1)
    sim.print_world(farmland)
    print()

    # print("player1:", farmland.get_player())

    # print("f1:")
    # for row in farmland.get_grid():
    #     print(row)


# def main():
#     farmland = World("Myers Farm", "test.csv")
#     player1 = Actor("hugright")
#
#     farmland.add_player(player1)
#     print(f"Player is `{farmland.get_player()}`")


if __name__ == "__main__":
    # main()
    test()
