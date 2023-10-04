class Monster:
    def __init__(self, health: int, attack: int, speed: int):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health


goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(goblin.get_health())

wolf = Monster(1000, 200, 500)
wolf.decrease_health(200)
print(wolf.get_health())

# 파이썬에서는 자료형도 클래스다.
# a = 10
# b = "문자열"
# c = True

# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'str'>
# print(type(c))  # <class 'bool'>
# print(b.__dir__())
