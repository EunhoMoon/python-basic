# 대입 연산: 변수이름 = 데이터

# 산술연산
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print(x ** y) # 제곱

# 문자열 연산
tag1 = "#태그1"
tag2 = "#태그2"
tag3 = "#태그3"

tag = tag1 + tag2 + tag3
print(tag)

message = "test\n" * 3
print(message)

# 복합 할당 연산자
level = 10
level += 1

health = 1000
health -= 100

attack = 300
attack *= 1.5

speed = 420
speed /= 2

print(level, health, attack, speed)