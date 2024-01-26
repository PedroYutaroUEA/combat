import random
from wall import Wall


class Maze:
    def __init__(self):
        self.wall = Wall()
        self.pattern = random.randint(1, 10)
        self.walls = [1, 2, 3, 4, 5]

    def spawn_map(self):
        print(f"spawned N-{self.pattern} map type!")
