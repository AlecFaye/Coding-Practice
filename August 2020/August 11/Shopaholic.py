items = int(input())

costs_input = input().split()
costs = [int(x) for x in costs_input]
costs.sort()
costs.reverse()

total_saved = 0

for count in range(1, items // 3 + 1):
    total_saved += costs[count * 3 - 1]

print(total_saved)
