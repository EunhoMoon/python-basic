print('Hello Janek!')
print('You have 7 days left to use the premium service.')

print('Hello Moon!')
print('You have 30 days left to use the premium service.')

print('Hello Eunho!')
print('You have 21 days left to use the premium service.')

# def 함수이름(매개변수1, 매개변수2...) :
#   명령 블록
#   return 반환값

def printMessage(name, date):
    print(f'Hello {name}!') 
    print(f'You have {date} days left to use the premium service.')

printMessage('Janek', 7)
printMessage('Moon', 30)
printMessage('Eunho', 21)

def printHello():
    print('Hello')

printHello()

def sum(a, b):
    print(a + b)

sum(1, 2)

import random
def getRandomNumber():
    return random.randint(1, 100)

number = getRandomNumber()
print(number)