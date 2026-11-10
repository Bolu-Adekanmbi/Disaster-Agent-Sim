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

        for row in reader:
            print(row)


class World:
    def __init__(self, name, config):
        self.name = name
        self.map = process_config(config)
