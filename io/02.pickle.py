import pickle

data = {
    "goal1": "파이썬 기초 문법을 익힌다.",
    "goal2": "파이썬 심화 문법을 익힌다.",
}

file = open("data.pickle", "wb")
pickle.dump(data, file)
file.close()

# file = open("data.pickle", "rb")
# data = pickle.load(file)
# print(data)
# file.close()

# with 구문 사용시 자동으로 close()를 호출해준다.
with open("data.pickle", "rb") as file:
    data = pickle.load(file)
    print(data)