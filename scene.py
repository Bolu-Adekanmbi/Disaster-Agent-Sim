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

    # Where we store world info from processed config, returned by the function
    world_info = {}

    # Process the config as CSV
    with open(path, mode="r", newline="") as file:
        reader = csv.reader(file)

        r = 0  # row counters
        for row in reader:
            # print(row)
            c = 0  # col counter resets each row
            for val in row:
                # print(f"row {r} col {c} : {val}")
                if val == "p":
                    world_info["player_start"] = (r, c)
                c += 1
            r += 1
    return world_info


class World:
    def __init__(self, name, config):
        self.name = name
        self.map_config = process_config(config)
        self.player_start = self.map_config.get("player_start")

    def get_player_start(self):
        return self.player_start
