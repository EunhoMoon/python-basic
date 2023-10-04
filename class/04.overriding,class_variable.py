import random


class Monster:
    max_num = 1000  # 클래스 변수, 모든 인스턴스가 공유한다.

    def __init__(self, health: int, attack: int, speed: int):
        self.health = health
        self.attack = attack
        self.speed = speed
        Monster.max_num -= 1

    def move(self):
        print("지상에서 이동하기")


class Wolf(Monster):
    pass  # 아무것도 하지 않는다는 의미


class Shark(Monster):
    def move(self):
        print("헤엄치기")


class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, health: int, attack: int, speed: int):
        super().__init__(health, attack, speed)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):
        print("날기")

    def skill(self):
        print(f"스킬 사용: [{self.skills[random.randint(0, 2)]}]")


wolf = Wolf(1000, 200, 500)
wolf.move()
print(wolf.max_num)

shark = Shark(1000, 200, 500)
shark.move()
print(shark.max_num)

dragon = Dragon(1000, 200, 500)
dragon.move()
dragon.skill()
print(dragon.max_num)
