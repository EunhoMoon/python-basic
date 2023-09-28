# 데이터가 있는 리스트
animals = ["사자", "호랑이", "코끼리", "기린"]

# 데이터가 없는 리스트
empty_list = []

print(animals[2])  # 코끼리
print(animals[-1])  # 마지막 데이터

animals.append("코뿔소")  # 데이터 추가
print(animals)

animals[1] = "물범"  # 데이터 삽입
print(animals)

del animals[0]  # 데이터 삭제
print(animals)

print(animals[1:3]) # 데이터 슬라이싱
print(animals[:])   # 전체 데이터  
print(animals[:3])  # 0 ~ 2번째 데이터
print(animals[1:])  # 1 ~ 마지막 데이터

print(len(animals)) # 데이터 길이

animals.sort() # 오름차순 정렬
print(animals)

animals.reverse() # 내림차순 정렬
print(animals)