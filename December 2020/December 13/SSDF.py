cases = int(input())

for x in range(cases):
    sum_squared_digits = 0
    test, base, number = list(map(int, input().split()))

    while number > 0:
        sum_squared_digits += ((number % base) ** 2)
        number //= base

    print(test, sum_squared_digits)
