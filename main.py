from scene import World
from agent import Actor


def test():
    farmland = World("Myers Farm", "test.csv")
    player1 = Actor("hugright")
    farmland.add_player(player1)

    print("f1:")
    for row in farmland.get_grid():
        print(row)


# def main():
#     farmland = World("Myers Farm", "test.csv")
#     player1 = Actor("hugright")
#
#     farmland.add_player(player1)
#     print(f"Player is `{farmland.get_player()}`")


if __name__ == "__main__":
    # main()
    test()
