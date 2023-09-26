# 조건문
origin_pass = "1234"
input_pass = input("비밀번호를 입력하세요: ")

if origin_pass == input_pass:
    print("로그인 성공")
elif input_pass.strip()  == "":
    print("비밀번호를 입력하세요")
else:
    print("로그인 실패")