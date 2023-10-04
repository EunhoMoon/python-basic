class Monster:
    def say(self):
        print("Im Monster!")

goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다.
a = 10
b = "문자열"
c = True

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'bool'>

print(b.__dir__())