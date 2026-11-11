from scene import World
from agent import Actor


def main():
    farmland = World("Myers Farm", "test.csv")
    farmland2 = World("Myers Farm 2", "test2.csv")
    player1 = Actor("hugright")

    farmland.add_player(player1)
    print(f"Player is `{farmland.get_player()}`")

    print(farmland2)


if __name__ == "__main__":
    main()
