x = input()
expenses = list(map(int, input().split()))
total = 0

for cost in expenses:
    if cost < 0:
        total += cost

print(abs(total))
