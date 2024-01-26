from bullet import Bullet


class Tank:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.bullet = Bullet()
        print(f"Tank created at {x, y}")

    def shoot(self, d_x, d_y):
        print(f'tank {self.name} shoots on direction {d_x, d_y}!')

    def move(self, x, y):
        print(f'tank {self.name} goes to {x, y}')
