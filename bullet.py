class Bullet:
    def __init__(self):
        print("Bullet is created")

    @staticmethod
    def move(x, y):
        print(f"Bullet goes to {x, y}")
