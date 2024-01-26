import random
import sympy
from tank import Tank
from bullet import Bullet
from maze import Maze


class Game:
    def __init__(self):
        self.tank_a = Tank('A', 0, 25)
        self.tank_b = Tank('B', 50, 25)
        self.bullet = Bullet()
        self.maze = Maze()
        self.running = True

    def start_game(self):
        while self.running:
            # spawns everything
            print("Initialized game!")
            self.maze.spawn_map()
            print(f"spawned tank {self.tank_a.name}")
            print(f"spawned tank {self.tank_b.name}")
            tank_b_pos = (self.tank_b.x, self.tank_b.y)
            tank_a_pos = (self.tank_a.x, self.tank_a.y)
            # choosing user tank name
            t = input(f"'A' = tank {self.tank_a.name} shoots, 'B' = tank {self.tank_b.name} shoots: ").upper()
            while t not in ('A', 'B'):
                t = input(f"'A' = tank {self.tank_a.name} shoots, 'B' = tank {self.tank_b.name} shoots: ").upper()
            # tank auto-shoots based on user choice
            if t == 'A':
                self.tank_a.shoot()
            else:
                self.tank_b.shoot()
            # checks artificial bullet collision with enemy tank
            bullet_pos = (self.tank_a.x, self.tank_a.y) if t == 'A' else (self.tank_b.x, self.tank_b.y)
            while bullet_pos != (tank_b_pos if t == 'A' else tank_a_pos):
                # updates bullet position randomly
                r_x = random.randint(0, 50)
                r_y = random.randint(0, 50)
                bullet_pos = (r_x, r_y)
                # checks artificial bullet collision with wall
                if sympy.isprime(r_x) and sympy.isprime(r_y):
                    print(f"Bullet collides with wall {self.maze.walls[random.randint(0, 4)]}")
                self.bullet.move(r_x, r_y)
            # end of the round
            print(f"tank {self.tank_b.name if t == 'A' else self.tank_a.name} destroyed!")
            play = input("wanna play again (Y/N)?: ").upper()
            while play not in ('Y', 'N'):
                play = input("wanna play again (Y/N)?: ").upper()
            self.running = True if play == 'Y' else False
