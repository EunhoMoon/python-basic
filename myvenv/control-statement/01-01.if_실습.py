subscribe = int(input('현재 구독자 수를 입력하세요: '))

if subscribe >= 1000:
    print("수익 창출이 가능합니다.")
else :
    print("수익 창출이 불가능합니다.")


study_time = int(input('공부 시간을 입력하세요: '))

if study_time >= 10:
    print('휴대폰 잠금이 해제되었습니다.')
elif study_time >= 5:
    print('휴대폰을 30분간 사용할 수 있습니다.')
else:
    print('휴대폰을 사용할 수 없습니다.')

having_price = int(input('보유 금액을 입력하세요: '))

if having_price >= 20000:
    print('오늘 저녁은... 치킨이닭!')
elif having_price >= 12000:
    print('오늘 저녁은... 떡볶이!')
elif having_price >= 2000:
    print('오늘 저녁은... 편의점 김밥!')


korean = int(input('국어 점수를 입력하세요: '))
math = int(input('수학 점수를 입력하세요: '))
english = int(input('영어 점수를 입력하세요: '))

avg = (korean + math + english) / 3
if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100 :
    print('잘못 입력하였습니다.')
elif avg >= 80 :
    print('불합격')
else :
    print('합격')