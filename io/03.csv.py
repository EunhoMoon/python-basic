import csv

data = [
    ["name", "class", "score"],
    ["Janek", "A", 100],
    ["EunHo", "B", 200],
    ["Moon", "C", 300]
]

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    # for row in data:
    #     writer.writerow(row)
    writer.writerows(data)

with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
