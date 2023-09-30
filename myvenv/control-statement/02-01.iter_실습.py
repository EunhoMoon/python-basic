number = int(input('몇 단을 출력할까요?: '))

for i in range(1, 10):
    print(f'{number} * {i} = {number * i}')

words = ['안녕', '사자', '아침']

is_answer = True
while is_answer:
    for word in words:
        is_answer = word == input(f'{word}: ')
        if not is_answer:
            print('틀렸습니다.')
            break