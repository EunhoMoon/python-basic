# dictionary: map과 비슷한 자료형
#  - key와 value를 한 쌍으로 갖는 자료형
#  - 시퀀스 자료형
#  - 사전형태의 자료를 만들 때 편리
stock_a = {"삼성전자": 82000, "LG전자": 160000, "네이버": 500000}

stock_b = {
    "삼성전자": [81000, 82000, 80000, 82000, 81000],
    "LG전자": (160000, 160500, 161000, 160500, 160000),
}

stock_c = {
    "삼성전자": {
        "시가": 81000,
        "종가": 82000,
        "고가": 82000,
        "저가": 80000,
        "거래량": 81000,
    },
}

print(stock_a)
print(stock_b)
print(stock_c)

print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["시가"])

# 할당
stock_a["삼성전자"] = 85000

# 삭제
del stock_a["삼성전자"]
print(stock_a)

# 함수
stock_d = {"삼성전자": 82000, "LG전자": 160000, "네이버": 500000, "카카오": 500000}

print(stock_d.items())
print(stock_d.keys())
print(stock_d.values())

for item in stock_d.items():
    print(item)