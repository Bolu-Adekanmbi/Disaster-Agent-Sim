from pathlib import Path
import csv
from moves import Move


def process_config(config):
    path = Path(config)

    if path.suffix.lower() != ".csv":
        raise ValueError(f"World config must be a CSV file: {path}")
    if not path.exists():
        raise FileNotFoundError(f"World config file does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"World config path is not a file: {path}")

    with path.open(mode="r", newline="", encoding="utf-8-sig") as file:
        try:
            grid = [row for row in csv.reader(file) if row]
        except csv.Error as error:
            raise ValueError(f"Invalid CSV in world config {path}: {error}") from error

    if not grid:
        raise ValueError(f"World config CSV is empty: {path}")

    width = len(grid[0])
    if width == 0 or any(len(row) != width for row in grid):
        raise ValueError(f"World config must contain a non-empty rectangular grid: {path}")

    height = len(grid)
    player_positions = [
        (row_index, column_index)
        for row_index, row in enumerate(grid)
        for column_index, cell in enumerate(row)
        if cell == "p"
    ]
    if len(player_positions) != 1:
        raise ValueError(
            f"World config must contain exactly one player start 'p', found {len(player_positions)}: {path}"
        )

    if height < 3 or width < 3:
        raise ValueError(f"World config must be at least 3 rows by 3 columns: {path}")

    boundary_cells = (
        grid[0]
        + grid[-1]
        + [row[0] for row in grid[1:-1]]
        + [row[-1] for row in grid[1:-1]]
    )
    if any(cell != "#" for cell in boundary_cells):
        raise ValueError(f"World config must have '#' on every outer boundary cell: {path}")

    return {"grid": grid, "player_start": player_positions[0]}


class World:
    def __init__(self, name, config):
        self.name = name
        self.map_config = process_config(config)
        self.grid = self.map_config.get("grid")
        self.player_start = self.map_config.get("player_start")
        self.player_location = self.player_start
        self.player = None  # Perhaps with the simulator managing player matching there isn't a need for storing player in World

    def get_player_start(self):
        return self.player_start

    def get_player(self):
        if self.player is None:
            print(f"There is currently no player in the world `{self.name}`")
        return self.player

    def add_player(self, player):
        if self.player:
            print(
                f"The player `{self.player}` has already been added to the world, remove player first before adding a new one"
            )
        self.player = player

    def remove_player(self):
        self.player = None

    def get_grid(self):
        return self.grid

    def update(self, move):
        if not isinstance(move, Move):
            return False

        row, column = self.player_location
        destination = self.player_location
        for _ in range(move.magnitude):
            row += move.direction.row_change
            column += move.direction.column_change
            if not (0 <= row < len(self.grid) and 0 <= column < len(self.grid[row])):
                return False
            if self.grid[row][column] != "=":
                return False
            destination = (row, column)

        old_row, old_column = self.player_location
        new_row, new_column = destination
        self.grid[old_row][old_column] = "="
        self.grid[new_row][new_column] = "p"
        self.player_location = destination
        return True

    def __str__(self):
        return f"World: {self.name}\nPlayer Start: {self.player_start}\nPlayer: {self.player}"
