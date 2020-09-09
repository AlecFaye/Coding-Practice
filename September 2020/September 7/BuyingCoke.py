cases = int(input())
cost = 8

for test in range(cases):
    coke, one, five, ten = map(int, input().split())
    coins = 0

    # Attempt 1
    while coke > 0:
        if ten >= 1:
            ten -= 1
            one += 2
            coins += 1
        elif five >= 2:
            five -= 2
            one += 2
            coins += 2
        elif five >= 1:
            five -= 1
            one -= 3
            coins += 4
        else:
            one -= 8
            coins += 8
        coke -= 1

    print(coins)
