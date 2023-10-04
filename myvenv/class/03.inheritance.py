class Monster:
    def __init__(self, health: int, attack: int, speed: int):
        self.health = health
        self.attack = attack
        self.speed = speed

    def move(self):
        print("지상에서 이동하기")


class Wolf(Monster):
    pass  # 아무것도 하지 않는다는 의미


class Shark(Monster):
    def move(self):
        print("헤엄치기")


class Dragon(Monster):
    def move(self):
        print("날기")


wolf = Wolf(1000, 200, 500)
wolf.move()

shark = Shark(1000, 200, 500)
shark.move()

dragon = Dragon(1000, 200, 500)
dragon.move()
