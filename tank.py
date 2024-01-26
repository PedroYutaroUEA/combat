from bullet import Bullet


class Tank:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.bullet = Bullet()
        print(f"Tank created at {x, y}")

    def shoot(self):
        print(f'tank {self.name} shoots bullet!')
        # initial bullet position
        self.bullet.move(self.x + 1, self.y + 1)

    def move(self, x, y):
        print(f'tank {self.name} goes to {x, y}')
