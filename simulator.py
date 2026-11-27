class Simulator:
    def __init__(self):
        self.world = []
        self.actors = []
        self.current_world = None
        self.current_world_index = -1

        self.current_actor = None
        self.current_actor_index = -1

        self.world_count = 0
        self.actor_count = 0

        self.move_count = 0  # Might be better handled in the world class since we might end up with multiple worlds and actors in parallel with different move counts, but ok for now

    def add_world(self, world):
        self.world.append(world)
        self.world_count += 1
        self.current_world_index = self.world_count - 1

        # Current world is the first world added to the simulator, if no other world is set
        if self.current_world is None:
            self.current_world = world

    def add_actor(self, actor):
        self.actors.append(actor)
        self.actor_count += 1
        self.current_actor_index = self.actor_count - 1

        # Current actor is the first actor added to the simulator, if no other actor is set
        if self.current_actor is None:
            self.current_actor = actor

    def set_current_world(self, world_index):
        self.current_world = self.world[world_index]
        self.current_world_index = world_index

    def set_current_actor(self, actor_index):
        self.current_actor = self.actors[actor_index]
        self.current_actor_index = actor_index

    def sim_step(self, world, actor):
        next_move = actor.next_move(world)
        world.update(next_move)

        self.move_count += 1

    def print_world(self, world):
        for row in world.get_grid():
            print(row)
