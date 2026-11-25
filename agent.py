class Actor:
    def __init__(self, name):
        self.name = name
        self.strategy = None

    def __str__(self):
        return self.name

    def next_move(self, world):
        if world:
            return "forward"  # placeholder for now, will implement strategy later, and maybe a move class
