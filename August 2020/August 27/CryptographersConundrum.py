phrase = input()

days = 0

for index in range(0, len(phrase), 3):
    if phrase[index] != "P":
        days += 1
    if phrase[index + 1] != "E":
        days += 1
    if phrase[index + 2] != "R":
        days += 1

print(days)
