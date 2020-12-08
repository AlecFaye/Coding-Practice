questions = input().split(";")
total = 0

for x in questions:
    x = x.split("-")
    if len(x) > 1:
        total += int(x[1]) - int(x[0]) + 1
    else:
        total += 1

print(total)
