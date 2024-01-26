import random
from wall import Wall


class Maze:
    def __init__(self):
        self.wall = Wall()
        self.walls = [self.wall for _ in range(5)]

    def spawn_map(self):
        print(f"spawned N-{random.randint(1, 10)} map type with {len(self.walls)} walls!")
