from scene import World
from agent import Actor


def main():
    place1 = World("farmland1", "test.csv")
    player = Actor("hugright")

    print(f"Player start is: {place1.get_player_start()}")


if __name__ == "__main__":
    main()
