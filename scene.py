from pathlib import Path
import csv


def process_config(config):
    path = Path(config)

    # Check if the path exists and is a file
    if path.exists() and path.is_file():
        print("World config file exists, initiating processing...")
    else:
        print(f"The config file `{str(path)}` does not exist")

    # Check that it is a valid config file (CSV for now)
    # Check rules like world boundaries, roads exists, some disaster etc.

    # Process the config as CSV
    with open(path, mode="r", newline="") as file:
        reader = csv.reader(file)

        r, c = 0, 0  # row and column counters
        for row in reader:
            # print(row)
            for val in row:
                print(f"row {r} col {c} : {val}")
                if val == "p":
                    return {"player_start": (r, c)}
                c += 1
            r += 1


class World:
    def __init__(self, name, config):
        self.name = name
        self.map_config = process_config(config)
        self.player_start = self.map_config.get("player_start")
        print(f"player_start: {self.player_start}")
