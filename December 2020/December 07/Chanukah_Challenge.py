cases = int(input())

for test in range(cases):
    n, days = list(map(int, input().split()))
    print(n, int(((days * (days + 1))/2 + days)))
