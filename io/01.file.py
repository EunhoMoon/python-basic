# Write a file: 'w'
file = open("data.txt", "w", encoding="utf-8")
file.write("Hello World!")
file.close()

# Append a file: 'a'
file = open("data.txt", "a", encoding="utf-8")
file.write("\n안녕 파이썬!")
file.close()

# Read a file: 'r'
file = open("data.txt", "r", encoding="utf-8")
data = file.read()
print(data)
file.close()

# Read a file line by line: 'r'
file = open("data.txt", "r", encoding="utf-8")
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()
