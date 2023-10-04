champions = ['Liverpool', 'Chelsea', 'Arsenal', 'Manchester City', 'Manchester United']

for champion in champions:
    print(f'{champion} is a champion.')

message = '파이팅'
for word in message:
    print(word)

for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 5, 2):
    print(i)

i = 0
while i < 5:
    print(f'{i}번째 반복입니다.')
    i += 1

while True:
    x = input('종료하려면 exit를 입력하세요: ')
    if x == 'exit':
        break