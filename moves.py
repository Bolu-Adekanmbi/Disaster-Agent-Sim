from dataclasses import dataclass


@dataclass(frozen=True)
class Direction:
    name: str
    row_change: int
    column_change: int
    description: str


@dataclass(frozen=True)
class Move:
    direction: Direction
    magnitude: int = 1

    def __post_init__(self):
        if not isinstance(self.magnitude, int) or isinstance(self.magnitude, bool):
            raise TypeError("Move magnitude must be an integer")
        if self.magnitude < 1:
            raise ValueError("Move magnitude must be at least 1")

    @property
    def description(self):
        return f"{self.direction.description} by {self.magnitude} cell(s)"


UP = Direction("up", -1, 0, "Move up")
DOWN = Direction("down", 1, 0, "Move down")
LEFT = Direction("left", 0, -1, "Move left")
RIGHT = Direction("right", 0, 1, "Move right")
