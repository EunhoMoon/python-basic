# 내장 모듈: 파이썬이 기본적으로 제공하는 모듈
# import math
from math import pi, ceil as c

print(pi)
# print(ceil(2.7))
print(c(2.7))

# 외부 모듈: 다른 사람이 만들어서 제공하는 모듈
import pyautogui as pg

pg.moveTo(100, 100, duration=2)
