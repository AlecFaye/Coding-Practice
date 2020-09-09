cases = int(input())

for test in range(cases):
    turtle_count = input().split()
    imported = 0

    for index in range(1, len(turtle_count) - 1):
        current = int(turtle_count[index])
        previous = int(turtle_count[index - 1])
        calculate = current - previous * 2
        if calculate > 0:
            imported += current - previous * 2

    print(imported)
