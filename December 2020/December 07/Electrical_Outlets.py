cases = int(input())

for test in range(cases):
    outlets = input().split()
    count = int(outlets[0])
    max_app = 0

    for x in range(1, count + 1):
        max_app += int(outlets[x])

    print(max_app - count + 1)
