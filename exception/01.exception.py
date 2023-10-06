won = input("원화금액을 입력하세요: ")
dollar = input("환율을 입력하세요: ")

try:
    print(int(won) / int(dollar))
except ValueError as error:
    print("숫자만 입력하세요", error)
except ZeroDivisionError as error:
    print("환율은 0이 될 수 없습니다.", error)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드.")
finally:
    print("예외 발생 여부와 상관없이 항상 실행되는 코드.")