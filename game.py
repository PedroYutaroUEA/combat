import random
import sympy
from tank import Tank
from bullet import Bullet
from maze import Maze


class Game:
    def __init__(self):
        self.t_a_pos = (0, 25)
        self.t_b_pos = (50, 25)
        self.tank_a = Tank('A', self.t_a_pos[0], self.t_a_pos[1])
        self.tank_b = Tank('B', self.t_b_pos[0], self.t_b_pos[1])
        self.bullet = Bullet()
        self.maze = Maze()

    def start_game(self):
        print("Initialized game!")
        self.maze.spawn_map()
        print(f"spawned tank {self.tank_a.name}")
        print(f"spawned tank {self.tank_b.name}")
        # sets initial bullet position at the same position of tank A
        b_pos = (self.t_a_pos[0], self.t_a_pos[1])
        self.tank_a.shoot(b_pos[0], b_pos[1])
        self.bullet.move(b_pos[0] + 1, b_pos[1] + 1)
        # checks bullet (from tank A) collision with tank B
        while b_pos != self.t_b_pos:
            # updates bullet position randomly
            r_x = random.randint(0, 50)
            r_y = random.randint(0, 50)
            b_pos = (r_x, r_y)
            # checks artificial bullet collision with wall
            if sympy.isprime(r_x) and sympy.isprime(r_y):
                print(f"Bullet collides with wall {self.maze.walls[random.randint(0, 4)]}")
            self.bullet.move(r_x, r_y)
        print(f"tank {self.tank_b.name} destroyed!")
