cases = int(input())

for x in range(cases):
    test, number = list(map(int, input().split()))
    total = 0

    for count in range(1, number + 1):
        total += count
    print(test, total, total * 2 - number, total * 2)
