# tuple : 시퀀스 자료형
#  - read-only list: 수정, 추가, 삭제가 불가
#  - 메모리 사용이 효율적
#  - read-only이기 때문에 데이터 손실 염려가 없다.
a = (3, 4, 5)
b = 3, 4, 5

c = (3,)
d = 3,

e = tuple([3, 4, 5])
f = list(range(10))
g = tuple(f)

h = 3, 4, 5
i = list(h)

# tuple 관련 함수
x = 5, 6, 7, 8
print("max(): ", max(x))
print("min(): ", min(x))
print("sum(): ", sum(x))
print("count(): ", x.count(5))
print("index(): ", x.index(5))